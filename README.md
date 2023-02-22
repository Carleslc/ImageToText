# ImageToText

OCR ([*Optical Character Recognition*](https://en.wikipedia.org/wiki/Optical_character_recognition)) with Google's AI technology ([Cloud Vision API](https://cloud.google.com/vision/docs/ocr)).

The Vision API can detect and extract text from images.

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C2VFGD)

## Install

1. Download [Python 3.6+](https://www.python.org/downloads/) or follow [this guide from Google Cloud](https://cloud.google.com/python/setup).
2. Clone or [download](https://github.com/Carleslc/ImageToText/archive/refs/heads/master.zip) this repository.
3. Inside this repository, install the `img2txt` script from your terminal:
   
   ```sh
   pip install -e .
   ```

To uninstall: `pip uninstall ImageToText`

## Usage

```
usage: img2txt [-h] [--url] [--document] [--languages LANGUAGES] [--full] [--confidence CONFIDENCE] [--key KEY] path

positional arguments:
  path                  path to image

optional arguments:
  -h, --help            show this help message and exit
  --url                 specify the path for an external image located on the Web (http:// or https://) or in Google Cloud Storage (gs://)
  --document            optimized for dense images
  --languages LANGUAGES, --language LANGUAGES
                        specify language hints from https://cloud.google.com/vision/docs/languages (comma separated)
  --full, --verbose     show full description (paragraphs, per-word confidence, boundaries...)
  --confidence CONFIDENCE
                        display possible mistakes for symbols with low confidence. Default: 0.6
  --key KEY             explicitly define the path to your service account JSON credentials
```

## Authentication

Follow [these instructions](https://cloud.google.com/vision/docs/detect-labels-image-client-libraries#before-you-begin) to set up a project with the Cloud Vision API enabled:

1. [Select or create a Google Cloud Platform project](https://console.cloud.google.com/projectselector2). Project name suggestion: *ImageToText*
2. [Enable Cloud Vision API for your project](https://console.cloud.google.com/apis/library/vision.googleapis.com).
3. [Create a service account and get your JSON credentials](https://console.cloud.google.com/iam-admin/serviceaccounts/create). Service account name suggestion: *ImageToText*
4. [Make sure that billing is enabled for your project](https://console.cloud.google.com/billing/linkedaccount).
   
   Pricing is based on [Google Cloud Vision API quota](https://cloud.google.com/vision/pricing#prices): *1,000 requests/month free*

To authenticate your project you need to reference the service account JSON credentials you just downloaded.
You have different options to do it, choose what you prefer:

### service_account.json file

Rename the JSON you downloaded in step 3 to `service_account.json` and place it inside this repository folder.

### `--key` parameter

Another option is to explicitly specify the `--key` parameter on every script execution:

`img2txt abbey_road.jpg --key "/path/to/service_account.json"`

### Environment variable

You can also [set the ***GOOGLE_APPLICATION_CREDENTIALS*** environmental variable](https://cloud.google.com/docs/authentication/provide-credentials-adc#local-key):

<details>
  <summary><a><i>bash</i></a></summary>

  <p>Add to your <code>.bash_profile</code> file:</p>
  
  <code>export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service_account.json"</code>

</details>

<details>
  <summary><a><i>fish</i></a></summary>

  <p>Add to your <code>config.fish</code> file:</p>
  
  <code>set -gx GOOGLE_APPLICATION_CREDENTIALS "/path/to/service_account.json"</code>

</details>

## Examples

![abbey_road.JPG](https://cloud.google.com/vision/docs/images/abbey_road.JPG)

From file:

`img2txt abbey_road.jpg`

From any URL from the web:

`img2txt --url https://cloud.google.com/vision/docs/images/abbey_road.JPG`

```
Language: en

ABBEY
ROAD NW8
CITY OF WESTMINSTER
```

![sign.jpg](https://cloud.google.com/static/vision/docs/images/sign_small.jpg)

From Google Cloud Storage:

`img2txt --url gs://cloud-samples-data/vision/ocr/sign.jpg`

```
Language: en

WAITING?
PLEASE
TURN OFF
YOUR
ENGINE
```

With full description:

`img2txt --full --url https://cloud.google.com/static/vision/docs/images/sign_small.jpg`

```
Language: en

WAITING?
PLEASE
TURN OFF
YOUR
ENGINE
bounds: (52,143),(391,143),(391,343),(52,343)

WAITING
bounds: (59,143),(355,157),(353,197),(57,184)

?
bounds: (359,157),(391,158),(389,198),(357,197)

PLEASE
bounds: (211,214),(332,219),(331,241),(210,236)

TURN
bounds: (213,246),(299,249),(298,271),(212,268)

OFF
bounds: (313,250),(372,252),(371,273),(312,271)

YOUR
bounds: (211,281),(303,283),(303,304),(211,302)

ENGINE
bounds: (213,315),(336,318),(335,340),(212,337)
```

![Example image in spanish](https://i.imgur.com/7YhDbGf.jpg)

With dense documents:

`img2txt --document --url https://i.imgur.com/7YhDbGf.jpg`

Specify [language hints](https://cloud.google.com/vision/docs/languages) (Optional):

`img2txt --document --language "es" --url https://i.imgur.com/7YhDbGf.jpg`

```
Language: es

Existen otras razones por las que masticar los alimentos como es debido es algo
esencial para nuestro bienestar. Según un fascinante estudio de investigación rea-
lizado en la Universidad de Gifu, en Japón, la masticación mejora la memoria al
reducir la liberación de las hormonas del estrés. La técnica de formación de ima-
gen por resonancia magnética (IRM) muestra que la masticación estimula el hi-
pocampo, el cual, a su vez, ayuda a controlar los niveles de hormonas del estrés en
sangre. El resultado es que el simple acto de masticar reduce tanto el estrés como
las hormonas del estrés, de modo que masticar bien los alimentos puede reducir
efectivamente el grado de ansiedad.
Los científicos japoneses descubrieron también que cuando faltan dientes o és-
tos se hallan en mal estado, se suele masticar menos. Ello hace que, acto seguido,
aumenten los niveles de hormonas del estrés. La conclusión de este estudio es que
una buena salud dental y una adecuada masticación son factores muy importantes
para conservar la memoria cuando envejecemos y para protegernos de los dañinos
efectos del estrés.
Una vez ha pasado por el esófago, el alimento entra en el estómago. Si lo que co-
memos contiene hidratos de carbono (azúcares complejos y almidones como los que
se encuentran
```

With full description:

`img2txt --full --document --url https://i.imgur.com/7YhDbGf.jpg`

```
Language: es

Existen otras razones por las que masticar los alimentos como es debido es algo
esencial para nuestro bienestar. Según un fascinante estudio de investigación rea-
lizado en la Universidad de Gifu, en Japón, la masticación mejora la memoria al
reducir la liberación de las hormonas del estrés. La técnica de formación de ima-
gen por resonancia magnética (IRM) muestra que la masticación estimula el hi-
pocampo, el cual, a su vez, ayuda a controlar los niveles de hormonas del estrés en
sangre. El resultado es que el simple acto de masticar reduce tanto el estrés como
las hormonas del estrés, de modo que masticar bien los alimentos puede reducir
efectivamente el grado de ansiedad.
Los científicos japoneses descubrieron también que cuando faltan dientes o és-
tos se hallan en mal estado, se suele masticar menos. Ello hace que, acto seguido,
aumenten los niveles de hormonas del estrés. La conclusión de este estudio es que
una buena salud dental y una adecuada masticación son factores muy importantes
para conservar la memoria cuando envejecemos y para protegernos de los dañinos
efectos del estrés.
Una vez ha pasado por el esófago, el alimento entra en el estómago. Si lo que co-
memos contiene hidratos de carbono (azúcares complejos y almidones como los que
se encuentran

SINGLE LINE

Existen otras razones por las que masticar los alimentos como es debido es algo esencial para nuestro bienestar. Según un fascinante estudio de investigación realizado en la Universidad de Gifu, en Japón, la masticación mejora la memoria al reducir la liberación de las hormonas del estrés. La técnica de formación de imagen por resonancia magnética (IRM) muestra que la masticación estimula el hipocampo, el cual, a su vez, ayuda a controlar los niveles de hormonas del estrés en sangre. El resultado es que el simple acto de masticar reduce tanto el estrés como las hormonas del estrés, de modo que masticar bien los alimentos puede reducir efectivamente el grado de ansiedad. Los científicos japoneses descubrieron también que cuando faltan dientes o éstos se hallan en mal estado, se suele masticar menos. Ello hace que, acto seguido, aumenten los niveles de hormonas del estrés. La conclusión de este estudio es que una buena salud dental y una adecuada masticación son factores muy importantes para conservar la memoria cuando envejecemos y para protegernos de los dañinos efectos del estrés. Una vez ha pasado por el esófago, el alimento entra en el estómago. Si lo que comemos contiene hidratos de carbono (azúcares complejos y almidones como los que se encuentran

PARAGRAPHS

--
Existen otras razones por las que masticar los alimentos como es debido es algo esencial para nuestro bienestar. Según un fascinante estudio de investigación realizado en la Universidad de Gifu, en Japón, la masticación mejora la memoria al reducir la liberación de las hormonas del estrés. La técnica de formación de imagen por resonancia magnética (IRM) muestra que la masticación estimula el hipocampo, el cual, a su vez, ayuda a controlar los niveles de hormonas del estrés en sangre. El resultado es que el simple acto de masticar reduce tanto el estrés como las hormonas del estrés, de modo que masticar bien los alimentos puede reducir efectivamente el grado de ansiedad.

Los científicos japoneses descubrieron también que cuando faltan dientes o éstos se hallan en mal estado, se suele masticar menos. Ello hace que, acto seguido, aumenten los niveles de hormonas del estrés. La conclusión de este estudio es que una buena salud dental y una adecuada masticación son factores muy importantes para conservar la memoria cuando envejecemos y para protegernos de los dañinos efectos del estrés.

Una vez ha pasado por el esófago, el alimento entra en el estómago. Si lo que comemos contiene hidratos de carbono (azúcares complejos y almidones como los que

se encuentran
--

Block confidence: 0.991

Existen otras razones por las que masticar los alimentos como es debido es algo esencial para nuestro bienestar. Según un fascinante estudio de investigación realizado en la Universidad de Gifu, en Japón, la masticación mejora la memoria al reducir la liberación de las hormonas del estrés. La técnica de formación de imagen por resonancia magnética (IRM) muestra que la masticación estimula el hipocampo, el cual, a su vez, ayuda a controlar los niveles de hormonas del estrés en sangre. El resultado es que el simple acto de masticar reduce tanto el estrés como las hormonas del estrés, de modo que masticar bien los alimentos puede reducir efectivamente el grado de ansiedad.

Paragraph confidence: 0.991

(0.992) Existen
(0.991) otras
(0.993) razones
(0.983) por
(0.992) las
(0.991) que
(0.993) masticar
(0.981) los
(0.994) alimentos
(0.991) como
(0.992) es
(0.994) debido
(0.989) es
(0.988) algo
(0.994) esencial
(0.993) para
(0.994) nuestro
(0.994) bienestar
(0.987) .
(0.992) Según
(0.996) un
(0.994) fascinante
(0.990) estudio
(0.994) de
(0.994) investigación
(0.988) rea
(0.990) lizado
(0.995) en
(0.994) la
(0.995) Universidad
(0.997) de
(0.992) Gifu
(0.988) ,
(0.996) en
(0.993) Japón
(0.986) ,
(0.986) la
(0.994) masticación
(0.995) mejora
(0.990) la
(0.995) memoria
(0.980) al
(0.985) reducir
(0.992) la
(0.994) liberación
(0.995) de
(0.995) las
(0.993) hormonas
(0.996) del
(0.992) estrés
(0.965) .
(0.994) La
(0.994) técnica
(0.998) de
(0.995) formación
(0.995) de
(0.965) ima
(0.991) gen
(0.989) por
(0.995) resonancia
(0.994) magnética
(0.987) (
(0.972) IRM
(0.975) )
(0.993) muestra
(0.995) que
(0.988) la
(0.992) masticación
(0.992) estimula
(0.996) el
(0.960) hi
(0.984) pocampo
(0.891) ,
(0.990) el
(0.992) cual
(0.972) ,
(0.985) a
(0.990) su
(0.992) vez
(0.984) ,
(0.990) ayuda
(0.992) a
(0.991) controlar
(0.982) los
(0.994) niveles
(0.990) de
(0.992) hormonas
(0.994) del
(0.980) estrés
(0.991) en
(0.991) sangre
(0.960) .
(0.974) El
(0.991) resultado
(0.992) es
(0.991) que
(0.989) el
(0.991) simple
(0.991) acto
(0.995) de
(0.994) masticar
(0.988) reduce
(0.993) tanto
(0.994) el
(0.971) estrés
(0.981) como
(0.991) las
(0.994) hormonas
(0.992) del
(0.994) estrés
(0.987) ,
(0.997) de
(0.997) modo
(0.995) que
(0.995) masticar
(0.995) bien
(0.996) los
(0.996) alimentos
(0.995) puede
(0.992) reducir
(0.996) efectivamente
(0.993) el
(0.988) grado
(0.986) de
(0.992) ansiedad
(0.945) .

Block confidence: 0.989

Los científicos japoneses descubrieron también que cuando faltan dientes o éstos se hallan en mal estado, se suele masticar menos. Ello hace que, acto seguido, aumenten los niveles de hormonas del estrés. La conclusión de este estudio es que una buena salud dental y una adecuada masticación son factores muy importantes para conservar la memoria cuando envejecemos y para protegernos de los dañinos efectos del estrés.

Paragraph confidence: 0.989

(0.980) Los
(0.976) científicos
(0.995) japoneses
(0.985) descubrieron
(0.985) también
(0.994) que
(0.994) cuando
(0.996) faltan
(0.994) dientes
(0.989) o
(0.903) és
(0.985) tos
(0.993) se
(0.994) hallan
(0.995) en
(0.994) mal
(0.991) estado
(0.986) ,
(0.993) se
(0.992) suele
(0.993) masticar
(0.995) menos
(0.987) .
(0.990) Ello
(0.992) hace
(0.993) que
(0.989) ,
(0.995) acto
(0.992) seguido
(0.935) ,
(0.993) aumenten
(0.990) los
(0.995) niveles
(0.995) de
(0.990) hormonas
(0.996) del
(0.990) estrés
(0.984) .
(0.993) La
(0.970) conclusión
(0.994) de
(0.996) este
(0.996) estudio
(0.995) es
(0.991) que
(0.985) una
(0.993) buena
(0.986) salud
(0.992) dental
(0.995) y
(0.994) una
(0.996) adecuada
(0.993) masticación
(0.995) son
(0.995) factores
(0.995) muy
(0.993) importantes
(0.994) para
(0.996) conservar
(0.992) la
(0.993) memoria
(0.994) cuando
(0.993) envejecemos
(0.991) y
(0.991) para
(0.992) protegernos
(0.993) de
(0.985) los
(0.950) dañinos
(0.995) efectos
(0.993) del
(0.971) estrés
(0.933) .

Block confidence: 0.981

Una vez ha pasado por el esófago, el alimento entra en el estómago. Si lo que comemos contiene hidratos de carbono (azúcares complejos y almidones como los que

Paragraph confidence: 0.987

(0.988) Una
(0.986) vez
(0.978) ha
(0.995) pasado
(0.986) por
(0.991) el
(0.972) esófago
(0.994) ,
(0.989) el
(0.993) alimento
(0.995) entra
(0.994) en
(0.994) el
(0.983) estómago
(0.939) .
(0.975) Si
(0.984) lo
(0.978) que
(0.959) co
(0.991) memos
(0.995) contiene
(0.994) hidratos
(0.994) de
(0.993) carbono
(0.992) (
(0.984) azúcares
(0.990) complejos
(0.995) y
(0.988) almidones
(0.982) como
(0.985) los
(0.985) que

se encuentran

Paragraph confidence: 0.912

(0.951) se
(0.905) encuentran
```

![Handwriting example](https://cloud.google.com/static/vision/docs/images/detect_handwriting_OCR-detect-handwriting_SMALL.png)

With handwritten documents:

`img2txt --document --url https://cloud.google.com/static/vision/docs/images/detect_handwriting_OCR-detect-handwriting_SMALL.png --confidence 0.7`

```
Language: en

Google Cloud
Platform

Possible mistake: symbol 'u' in word 'Cloud' (confidence: 0.680)
Possible mistake: symbol 'P' in word 'Platform' (confidence: 0.639)
```

With full description:

`img2txt --document --url https://cloud.google.com/static/vision/docs/images/detect_handwriting_OCR-detect-handwriting_SMALL.png --confidence 0.7 --full`

```
Language: en

Google Cloud
Platform

SINGLE LINE

Google Cloud Platform

PARAGRAPHS

--
Google Cloud

Platform
--

Block confidence: 0.894

Google Cloud

Paragraph confidence: 0.917

(0.990) Google
(0.829) Cloud
Possible mistake: symbol 'u' in word 'Cloud' (confidence: 0.680)

Platform

Paragraph confidence: 0.862

(0.862) Platform
Possible mistake: symbol 'P' in word 'Platform' (confidence: 0.639)
```

### Alternative: Use <u>gcloud</u> CLI

To perform entity analysis, use the [`gcloud ml vision detect-text`](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-text) command using the [Google Cloud SDK](https://cloud.google.com/sdk/docs/) as shown in the following example:

```sh
gcloud auth login
gcloud projects list # check your PROJECT_ID (e.g. imagetotext)
gcloud config set project imagetotext
```

![abbey_road.JPG](https://cloud.google.com/vision/docs/images/abbey_road.png)

```
gcloud ml vision detect-text "https://cloud.google.com/vision/docs/images/abbey_road.JPG" > abbey_road.txt
```

`abbey_road.txt`

```
{
  "responses": [
    {
      "fullTextAnnotation": {
        "pages": [
          {
            "blocks": [
              {
                "blockType": "TEXT",
                "boundingBox": {
                  "vertices": [
                    {
                      "x": 43,
                      "y": 43
                    },
                    {
                      "x": 267,
                      "y": 40
                    },
                    {
                      "x": 269,
                      "y": 174
                    },
                    {
                      "x": 45,
                      "y": 177
                    }
                  ]
                },
                "paragraphs": [
                  {
                    "boundingBox": {
                      "vertices": [
                        {
                          "x": 43,
                          "y": 43
                        },
                        {
                          "x": 267,
                          "y": 40
                        },
                        {
                          "x": 268,
                          "y": 129
                        },
                        {
                          "x": 44,
                          "y": 132
                        }
                      ]
                    },
                    "words": [
                      {
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 43,
                              "y": 43
                            },
                            {
                              "x": 182,
                              "y": 41
                            },
                            {
                              "x": 182,
                              "y": 79
                            },
                            {
                              "x": 43,
                              "y": 81
                            }
                          ]
                        },
                        "property": {
                          "detectedLanguages": [
                            {
                              "confidence": 1.0,
                              "languageCode": "en"
                            }
                          ]
                        },
                        "symbols": [
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 43,
                                  "y": 44
                                },
                                {
                                  "x": 73,
                                  "y": 44
                                },
                                {
                                  "x": 73,
                                  "y": 81
                                },
                                {
                                  "x": 43,
                                  "y": 81
                                }
                              ]
                            },
                            "text": "A"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 73,
                                  "y": 43
                                },
                                {
                                  "x": 96,
                                  "y": 43
                                },
                                {
                                  "x": 96,
                                  "y": 80
                                },
                                {
                                  "x": 73,
                                  "y": 80
                                }
                              ]
                            },
                            "text": "B"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 103,
                                  "y": 43
                                },
                                {
                                  "x": 126,
                                  "y": 43
                                },
                                {
                                  "x": 126,
                                  "y": 80
                                },
                                {
                                  "x": 103,
                                  "y": 80
                                }
                              ]
                            },
                            "text": "B"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 131,
                                  "y": 42
                                },
                                {
                                  "x": 151,
                                  "y": 42
                                },
                                {
                                  "x": 151,
                                  "y": 79
                                },
                                {
                                  "x": 131,
                                  "y": 79
                                }
                              ]
                            },
                            "text": "E"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 154,
                                  "y": 42
                                },
                                {
                                  "x": 182,
                                  "y": 42
                                },
                                {
                                  "x": 182,
                                  "y": 79
                                },
                                {
                                  "x": 154,
                                  "y": 79
                                }
                              ]
                            },
                            "property": {
                              "detectedBreak": {
                                "type": "EOL_SURE_SPACE"
                              }
                            },
                            "text": "Y"
                          }
                        ]
                      },
                      {
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 46,
                              "y": 94
                            },
                            {
                              "x": 154,
                              "y": 92
                            },
                            {
                              "x": 155,
                              "y": 130
                            },
                            {
                              "x": 47,
                              "y": 132
                            }
                          ]
                        },
                        "property": {
                          "detectedLanguages": [
                            {
                              "confidence": 1.0,
                              "languageCode": "en"
                            }
                          ]
                        },
                        "symbols": [
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 46,
                                  "y": 95
                                },
                                {
                                  "x": 69,
                                  "y": 95
                                },
                                {
                                  "x": 70,
                                  "y": 132
                                },
                                {
                                  "x": 47,
                                  "y": 132
                                }
                              ]
                            },
                            "text": "R"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 72,
                                  "y": 94
                                },
                                {
                                  "x": 96,
                                  "y": 94
                                },
                                {
                                  "x": 97,
                                  "y": 131
                                },
                                {
                                  "x": 73,
                                  "y": 131
                                }
                              ]
                            },
                            "text": "O"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 98,
                                  "y": 94
                                },
                                {
                                  "x": 126,
                                  "y": 94
                                },
                                {
                                  "x": 127,
                                  "y": 131
                                },
                                {
                                  "x": 99,
                                  "y": 131
                                }
                              ]
                            },
                            "text": "A"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 130,
                                  "y": 93
                                },
                                {
                                  "x": 154,
                                  "y": 93
                                },
                                {
                                  "x": 155,
                                  "y": 130
                                },
                                {
                                  "x": 131,
                                  "y": 130
                                }
                              ]
                            },
                            "property": {
                              "detectedBreak": {
                                "type": "SPACE"
                              }
                            },
                            "text": "D"
                          }
                        ]
                      },
                      {
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 180,
                              "y": 92
                            },
                            {
                              "x": 268,
                              "y": 91
                            },
                            {
                              "x": 269,
                              "y": 129
                            },
                            {
                              "x": 181,
                              "y": 130
                            }
                          ]
                        },
                        "property": {
                          "detectedLanguages": [
                            {
                              "confidence": 1.0,
                              "languageCode": "en"
                            }
                          ]
                        },
                        "symbols": [
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 180,
                                  "y": 93
                                },
                                {
                                  "x": 204,
                                  "y": 93
                                },
                                {
                                  "x": 205,
                                  "y": 130
                                },
                                {
                                  "x": 181,
                                  "y": 130
                                }
                              ]
                            },
                            "text": "N"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 208,
                                  "y": 92
                                },
                                {
                                  "x": 244,
                                  "y": 91
                                },
                                {
                                  "x": 245,
                                  "y": 128
                                },
                                {
                                  "x": 209,
                                  "y": 129
                                }
                              ]
                            },
                            "text": "W"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 248,
                                  "y": 92
                                },
                                {
                                  "x": 268,
                                  "y": 92
                                },
                                {
                                  "x": 269,
                                  "y": 129
                                },
                                {
                                  "x": 249,
                                  "y": 129
                                }
                              ]
                            },
                            "property": {
                              "detectedBreak": {
                                "type": "LINE_BREAK"
                              }
                            },
                            "text": "8"
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "boundingBox": {
                      "vertices": [
                        {
                          "x": 49,
                          "y": 160
                        },
                        {
                          "x": 249,
                          "y": 157
                        },
                        {
                          "x": 249,
                          "y": 174
                        },
                        {
                          "x": 49,
                          "y": 177
                        }
                      ]
                    },
                    "words": [
                      {
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 49,
                              "y": 160
                            },
                            {
                              "x": 86,
                              "y": 159
                            },
                            {
                              "x": 86,
                              "y": 176
                            },
                            {
                              "x": 49,
                              "y": 177
                            }
                          ]
                        },
                        "property": {
                          "detectedLanguages": [
                            {
                              "confidence": 1.0,
                              "languageCode": "en"
                            }
                          ]
                        },
                        "symbols": [
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 49,
                                  "y": 161
                                },
                                {
                                  "x": 58,
                                  "y": 161
                                },
                                {
                                  "x": 58,
                                  "y": 177
                                },
                                {
                                  "x": 49,
                                  "y": 177
                                }
                              ]
                            },
                            "text": "C"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 60,
                                  "y": 160
                                },
                                {
                                  "x": 64,
                                  "y": 160
                                },
                                {
                                  "x": 64,
                                  "y": 176
                                },
                                {
                                  "x": 60,
                                  "y": 176
                                }
                              ]
                            },
                            "text": "I"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 64,
                                  "y": 160
                                },
                                {
                                  "x": 74,
                                  "y": 160
                                },
                                {
                                  "x": 74,
                                  "y": 176
                                },
                                {
                                  "x": 64,
                                  "y": 176
                                }
                              ]
                            },
                            "text": "T"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 75,
                                  "y": 160
                                },
                                {
                                  "x": 86,
                                  "y": 160
                                },
                                {
                                  "x": 86,
                                  "y": 176
                                },
                                {
                                  "x": 75,
                                  "y": 176
                                }
                              ]
                            },
                            "property": {
                              "detectedBreak": {
                                "type": "SPACE"
                              }
                            },
                            "text": "Y"
                          }
                        ]
                      },
                      {
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 94,
                              "y": 160
                            },
                            {
                              "x": 114,
                              "y": 160
                            },
                            {
                              "x": 114,
                              "y": 176
                            },
                            {
                              "x": 94,
                              "y": 176
                            }
                          ]
                        },
                        "property": {
                          "detectedLanguages": [
                            {
                              "confidence": 1.0,
                              "languageCode": "en"
                            }
                          ]
                        },
                        "symbols": [
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 94,
                                  "y": 160
                                },
                                {
                                  "x": 103,
                                  "y": 160
                                },
                                {
                                  "x": 103,
                                  "y": 176
                                },
                                {
                                  "x": 94,
                                  "y": 176
                                }
                              ]
                            },
                            "text": "O"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 106,
                                  "y": 160
                                },
                                {
                                  "x": 114,
                                  "y": 160
                                },
                                {
                                  "x": 114,
                                  "y": 176
                                },
                                {
                                  "x": 106,
                                  "y": 176
                                }
                              ]
                            },
                            "property": {
                              "detectedBreak": {
                                "type": "SPACE"
                              }
                            },
                            "text": "F"
                          }
                        ]
                      },
                      {
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 121,
                              "y": 159
                            },
                            {
                              "x": 249,
                              "y": 157
                            },
                            {
                              "x": 249,
                              "y": 174
                            },
                            {
                              "x": 121,
                              "y": 176
                            }
                          ]
                        },
                        "property": {
                          "detectedLanguages": [
                            {
                              "confidence": 1.0,
                              "languageCode": "en"
                            }
                          ]
                        },
                        "symbols": [
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 121,
                                  "y": 159
                                },
                                {
                                  "x": 136,
                                  "y": 159
                                },
                                {
                                  "x": 136,
                                  "y": 175
                                },
                                {
                                  "x": 121,
                                  "y": 175
                                }
                              ]
                            },
                            "text": "W"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 139,
                                  "y": 159
                                },
                                {
                                  "x": 147,
                                  "y": 159
                                },
                                {
                                  "x": 147,
                                  "y": 175
                                },
                                {
                                  "x": 139,
                                  "y": 175
                                }
                              ]
                            },
                            "text": "E"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 149,
                                  "y": 159
                                },
                                {
                                  "x": 159,
                                  "y": 159
                                },
                                {
                                  "x": 159,
                                  "y": 175
                                },
                                {
                                  "x": 149,
                                  "y": 175
                                }
                              ]
                            },
                            "text": "S"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 160,
                                  "y": 159
                                },
                                {
                                  "x": 169,
                                  "y": 159
                                },
                                {
                                  "x": 169,
                                  "y": 175
                                },
                                {
                                  "x": 160,
                                  "y": 175
                                }
                              ]
                            },
                            "text": "T"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 172,
                                  "y": 159
                                },
                                {
                                  "x": 184,
                                  "y": 159
                                },
                                {
                                  "x": 184,
                                  "y": 175
                                },
                                {
                                  "x": 172,
                                  "y": 175
                                }
                              ]
                            },
                            "text": "M"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 188,
                                  "y": 158
                                },
                                {
                                  "x": 193,
                                  "y": 158
                                },
                                {
                                  "x": 193,
                                  "y": 174
                                },
                                {
                                  "x": 188,
                                  "y": 174
                                }
                              ]
                            },
                            "text": "I"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 195,
                                  "y": 158
                                },
                                {
                                  "x": 204,
                                  "y": 158
                                },
                                {
                                  "x": 204,
                                  "y": 174
                                },
                                {
                                  "x": 195,
                                  "y": 174
                                }
                              ]
                            },
                            "text": "N"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 207,
                                  "y": 158
                                },
                                {
                                  "x": 216,
                                  "y": 158
                                },
                                {
                                  "x": 216,
                                  "y": 174
                                },
                                {
                                  "x": 207,
                                  "y": 174
                                }
                              ]
                            },
                            "text": "S"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 218,
                                  "y": 158
                                },
                                {
                                  "x": 227,
                                  "y": 158
                                },
                                {
                                  "x": 227,
                                  "y": 174
                                },
                                {
                                  "x": 218,
                                  "y": 174
                                }
                              ]
                            },
                            "text": "T"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 229,
                                  "y": 158
                                },
                                {
                                  "x": 237,
                                  "y": 158
                                },
                                {
                                  "x": 237,
                                  "y": 174
                                },
                                {
                                  "x": 229,
                                  "y": 174
                                }
                              ]
                            },
                            "text": "E"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 240,
                                  "y": 158
                                },
                                {
                                  "x": 249,
                                  "y": 158
                                },
                                {
                                  "x": 249,
                                  "y": 174
                                },
                                {
                                  "x": 240,
                                  "y": 174
                                }
                              ]
                            },
                            "property": {
                              "detectedBreak": {
                                "type": "LINE_BREAK"
                              }
                            },
                            "text": "R"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "height": 240,
            "property": {
              "detectedLanguages": [
                {
                  "confidence": 1.0,
                  "languageCode": "en"
                }
              ]
            },
            "width": 320
          }
        ],
        "text": "ABBEY\nROAD NW8\nCITY OF WESTMINSTER"
      },
      "textAnnotations": [
        {
          "boundingPoly": {
            "vertices": [
              {
                "x": 43,
                "y": 40
              },
              {
                "x": 269,
                "y": 40
              },
              {
                "x": 269,
                "y": 177
              },
              {
                "x": 43,
                "y": 177
              }
            ]
          },
          "description": "ABBEY\nROAD NW8\nCITY OF WESTMINSTER",
          "locale": "en"
        },
        {
          "boundingPoly": {
            "vertices": [
              {
                "x": 43,
                "y": 43
              },
              {
                "x": 182,
                "y": 41
              },
              {
                "x": 182,
                "y": 79
              },
              {
                "x": 43,
                "y": 81
              }
            ]
          },
          "description": "ABBEY"
        },
        {
          "boundingPoly": {
            "vertices": [
              {
                "x": 46,
                "y": 94
              },
              {
                "x": 154,
                "y": 92
              },
              {
                "x": 155,
                "y": 130
              },
              {
                "x": 47,
                "y": 132
              }
            ]
          },
          "description": "ROAD"
        },
        {
          "boundingPoly": {
            "vertices": [
              {
                "x": 180,
                "y": 92
              },
              {
                "x": 268,
                "y": 91
              },
              {
                "x": 269,
                "y": 129
              },
              {
                "x": 181,
                "y": 130
              }
            ]
          },
          "description": "NW8"
        },
        {
          "boundingPoly": {
            "vertices": [
              {
                "x": 49,
                "y": 160
              },
              {
                "x": 86,
                "y": 159
              },
              {
                "x": 86,
                "y": 176
              },
              {
                "x": 49,
                "y": 177
              }
            ]
          },
          "description": "CITY"
        },
        {
          "boundingPoly": {
            "vertices": [
              {
                "x": 94,
                "y": 160
              },
              {
                "x": 114,
                "y": 160
              },
              {
                "x": 114,
                "y": 176
              },
              {
                "x": 94,
                "y": 176
              }
            ]
          },
          "description": "OF"
        },
        {
          "boundingPoly": {
            "vertices": [
              {
                "x": 121,
                "y": 159
              },
              {
                "x": 249,
                "y": 157
              },
              {
                "x": 249,
                "y": 174
              },
              {
                "x": 121,
                "y": 176
              }
            ]
          },
          "description": "WESTMINSTER"
        }
      ]
    }
  ]
}
```
