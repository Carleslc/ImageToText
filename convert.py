#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os, io
import argparse
from collections import deque
from google.cloud import vision
from google.oauth2 import service_account

def set_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to image")
    parser.add_argument("--url", action="store_true", help="specify that path is an external image located in Google Cloud Storage (gs://) or on the Web (http:// or https://)")
    parser.add_argument("--document", action="store_true", help="optimize for dense images")
    parser.add_argument("--languages", "--language", help="specify language hints from https://cloud.google.com/vision/docs/languages (comma separated)", default='')
    parser.add_argument("--full", action="store_true", help="show full description (per-word confidence, boundaries, paragraphs...)")
    parser.add_argument("--key", help="explicitly define the path to your service account JSON credentials")
    args = parser.parse_args()

def f(n, decimals=3):
    return "{:.{}f}".format(n, decimals)

def set_credentials():
    global credentials
    credentials = service_account.Credentials.from_service_account_file(args.key or os.environ['GOOGLE_APPLICATION_CREDENTIALS'])

def detect_text(vision_image, language_hints=[], full=False):
    client = vision.ImageAnnotatorClient(credentials=credentials)
    image_context = vision.types.ImageContext(language_hints=language_hints)
    response = client.text_detection(image=vision_image, image_context=image_context)

    texts = response.text_annotations
    print(f"Language: {texts[0].locale}")

    if full:
        print('Texts:')
        for text in texts:
            print('\n' + text.description)
            vertices = ([f'({vertex.x},{vertex.y})' for vertex in text.bounding_poly.vertices])
            boundaries = ','.join(vertices)
            print(f'bounds: {boundaries}')
    else:
        print()
        print(texts[0].description.strip())

def extract_paragraphs(full_text_annotation):
    breaks = vision.enums.TextAnnotation.DetectedBreak.BreakType
    paragraphs = []
    lines = []

    for page in full_text_annotation.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                para = ""
                line = ""
                for word in paragraph.words:
                    for symbol in word.symbols:
                        line += symbol.text
                        if symbol.property.detected_break.type == breaks.SPACE:
                            line += ' '
                        if symbol.property.detected_break.type == breaks.EOL_SURE_SPACE:
                            line += ' '
                            lines.append(line)
                            para += line
                            line = ''
                        if symbol.property.detected_break.type == breaks.LINE_BREAK:
                            lines.append(line)
                            para += line
                            line = ''
                paragraphs.append(para)

    return deque(paragraphs), lines

def detect_document_text(vision_image, language_hints=[], full=False):
    client = vision.ImageAnnotatorClient(credentials=credentials)
    image_context = vision.types.ImageContext(language_hints=language_hints)
    response = client.document_text_detection(image=vision_image, image_context=image_context)

    text = response.text_annotations[0]

    print(f"Language: {text.locale}\n")
    print(text.description.strip())

    if full:
        paragraphs, lines = extract_paragraphs(response.full_text_annotation)
        print('\nSINGLE LINE\n')
        print(' '.join(map(str.strip, lines)))
        print('\nBLOCKS & PARAGRAPHS\n\n--')
        print('\n\n'.join(paragraphs) + '\n--')
    else:
        print()

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            if full:
                print(f'\nBlock confidence: {f(block.confidence)}')

            for paragraph in block.paragraphs:
                if full:
                    print('\n' + paragraphs.popleft())
                    print(f'\nParagraph confidence: {f(paragraph.confidence)}')

                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])
                    if full:
                        print(f'({f(word.confidence)}) {word_text}')

                    for symbol in word.symbols:
                        #print(f'\tSymbol: {symbol.text} (confidence: {symbol.confidence})')
                        if symbol.confidence < 0.8:
                            print(f"Possible mistake: symbol '{symbol.text}' in word '{word_text}' (confidence: {f(symbol.confidence)})")

def get_image_file(path):
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    return vision.types.Image(content=content)

def get_image_uri(uri):
    image = vision.types.Image()
    image.source.image_uri = uri
    return image

if __name__ == "__main__":
    set_args()

    convert = detect_document_text if args.document else detect_text
    get_image = get_image_uri if args.url else get_image_file

    language_hints = args.languages.split(',')

    try:
        set_credentials()
        convert(get_image(args.path), language_hints, args.full)
    except Exception as e:
        print(e)