# ImageToText

OCR ([*Optical Character Recognition*](https://en.wikipedia.org/wiki/Optical_character_recognition)) with Google's AI technology ([Cloud Vision API](https://cloud.google.com/vision/docs/ocr)).

The Vision API can detect and extract text from images.

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C2VFGD)

## Install

1. Download [Python 3.6+](https://www.python.org/downloads/) or follow [this guide from Google Cloud](https://cloud.google.com/python/setup).
2. Install Cloud Vision API for Python: `pip3 install --user --upgrade google-cloud-vision`

## Usage

```
usage: convert.py [-h] [--url] [--document] [--languages LANGUAGES] [--full]
                  [--key KEY]
                  path

positional arguments:
  path                  path to image

optional arguments:
  -h, --help            show this help message and exit
  --url                 specify that path is an external image located in
                        Google Cloud Storage (gs://) or on the Web (http:// or
                        https://)
  --document            optimize for dense images
  --languages LANGUAGES, --language LANGUAGES
                        specify language hints from
                        https://cloud.google.com/vision/docs/languages (comma
                        separated)
  --full                show full description (per-word confidence,
                        boundaries, paragraphs...)
  --key KEY             explicitly define the path to your service account
                        JSON credentials
```

### Authentication

Follow [these instructions](https://cloud.google.com/vision/docs/quickstart-client-libraries#client-libraries-install-python) to set up a project with the Cloud Vision API enabled:

1. [Select or create a Google Cloud Platform project](https://console.cloud.google.com/cloud-resource-manager). Project name suggestion: *ImageToText*
2. [Enable Cloud Vision API for your project](https://console.cloud.google.com/apis/library/vision.googleapis.com).
3. [Create a service account and get your JSON credentials](https://console.cloud.google.com/apis/credentials/wizard). Service account name suggestion: *ImageToText*
4. [Make sure that billing is enabled for your project](https://console.cloud.google.com/billing/linkedaccount). Pricing is based on [Google Cloud Vision API quota](https://cloud.google.com/vision/pricing): *1,000 requests/month free*

For authentication you can [set the ***GOOGLE_APPLICATION_CREDENTIALS*** environmental variable](https://cloud.google.com/docs/authentication/getting-started#setting_the_environment_variable), for example:

`export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service_account.json"` where `service_account.json` is the credentials file you downloaded in step 3.

Or specify the `--key` parameter on every script execution: `python3 convert.py abbey_road.jpg --key "/home/user/Downloads/service_account.json"`

### Examples

The following examples suppose the `GOOGLE_APPLICATION_CREDENTIALS` environmental variable is already set.

![abbey_road.JPG](https://cloud.google.com/vision/docs/images/abbey_road.JPG)

From file: `python3 convert.py abbey_road.jpg`

From Google Cloud Storage: `python3 convert.py --url gs://bucket-name-123/abbey_road.jpg`

From any URL from the web: `python3 convert.py --url https://cloud.google.com/vision/docs/images/abbey_road.JPG`

```
Language: en

ABBEY
ROAD NW8
CITY OF WESTMINSTER
```

With full description: `python3 convert.py --full --url gs://bucket-name-123/abbey_road.jpg`

```
Language: en
Texts:

ABBEY
ROAD NW8
CITY OF WESTMINSTER

bounds: (46,41),(269,41),(269,177),(46,177)

ABBEY
bounds: (46,44),(179,41),(180,81),(47,84)

ROAD
bounds: (47,95),(155,94),(155,133),(47,134)

NW8
bounds: (180,93),(269,92),(269,131),(180,132)

CITY
bounds: (50,161),(85,160),(85,176),(50,177)

OF
bounds: (95,161),(114,161),(114,177),(95,177)

WESTMINSTER
bounds: (122,161),(249,159),(249,175),(122,177)
```

![Example image in spanish](https://i.imgur.com/PDpvufk.jpg)

With dense documents: `python3 convert.py --document --url https://i.imgur.com/PDpvufk.jpg`

Specify [language hints](https://cloud.google.com/vision/docs/languages) (Optional): `python3 convert.py --document --language "es" --url https://i.imgur.com/PDpvufk.jpg`

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
Una vez ha pasado por el esofago, el alimento entra en el estómago. Si lo que co-
memos contiene hidratos de carbono (azúcares complejos y almidones como los que
se encuent

Possible mistake: symbol 'o' in word 'esofago' (confidence: 0.460)
Possible mistake: symbol 't' in word 'encuent' (confidence: 0.530)
```

With full description: `python3 convert.py --full --document --url https://i.imgur.com/PDpvufk.jpg`

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
Una vez ha pasado por el esofago, el alimento entra en el estómago. Si lo que co-
memos contiene hidratos de carbono (azúcares complejos y almidones como los que
se encuent

SINGLE LINE

Existen otras razones por las que masticar los alimentos como es debido es algo esencial para nuestro bienestar. Según un fascinante estudio de investigación realizado en la Universidad de Gifu, en Japón, la masticación mejora la memoria al reducir la liberación de las hormonas del estrés. La técnica de formación de imagen por resonancia magnética (IRM) muestra que la masticación estimula el hipocampo, el cual, a su vez, ayuda a controlar los niveles de hormonas del estrés en sangre. El resultado es que el simple acto de masticar reduce tanto el estrés como las hormonas del estrés, de modo que masticar bien los alimentos puede reducir efectivamente el grado de ansiedad. Los científicos japoneses descubrieron también que cuando faltan dientes o éstos se hallan en mal estado, se suele masticar menos. Ello hace que, acto seguido, aumenten los niveles de hormonas del estrés. La conclusión de este estudio es que una buena salud dental y una adecuada masticación son factores muy importantes para conservar la memoria cuando envejecemos y para protegernos de los dañinos efectos del estrés. Una vez ha pasado por el esofago, el alimento entra en el estómago. Si lo que comemos contiene hidratos de carbono (azúcares complejos y almidones como los que se encuent

BLOCKS & PARAGRAPHS

--
Existen otras razones por las que masticar los alimentos como es debido es algo esencial para nuestro bienestar. Según un fascinante estudio de investigación realizado en la Universidad de Gifu, en Japón, la masticación mejora la memoria al reducir la liberación de las hormonas del estrés. La técnica de formación de imagen por resonancia magnética (IRM) muestra que la masticación estimula el hipocampo, el cual, a su vez, ayuda a controlar los niveles de hormonas del estrés en sangre. El resultado es que el simple acto de masticar reduce tanto el estrés como las hormonas del estrés, de modo que masticar bien los alimentos puede reducir efectivamente el grado de ansiedad.

Los científicos japoneses descubrieron también que cuando faltan dientes o éstos se hallan en mal estado, se suele masticar menos. Ello hace que, acto seguido, aumenten los niveles de hormonas del estrés. La conclusión de este estudio es que una buena salud dental y una adecuada masticación son factores muy importantes para conservar la memoria cuando envejecemos y para protegernos de los dañinos efectos del estrés.

Una vez ha pasado por el esofago, el alimento entra en el estómago. Si lo que comemos contiene hidratos de carbono (azúcares complejos y almidones como los que

se encuent
--

Block confidence: 0.990

Existen otras razones por las que masticar los alimentos como es debido es algo esencial para nuestro bienestar. Según un fascinante estudio de investigación realizado en la Universidad de Gifu, en Japón, la masticación mejora la memoria al reducir la liberación de las hormonas del estrés. La técnica de formación de imagen por resonancia magnética (IRM) muestra que la masticación estimula el hipocampo, el cual, a su vez, ayuda a controlar los niveles de hormonas del estrés en sangre. El resultado es que el simple acto de masticar reduce tanto el estrés como las hormonas del estrés, de modo que masticar bien los alimentos puede reducir efectivamente el grado de ansiedad.

Paragraph confidence: 0.990
(0.990) Existen
(0.990) otras
(0.990) razones
(0.990) por
(0.990) las
(0.990) que
(0.990) masticar
(0.990) los
(0.990) alimentos
(0.990) como
(0.990) es
(0.990) debido
(0.990) es
(0.990) algo
(0.990) esencial
(1.000) para
(0.990) nuestro
(0.990) bienestar
(0.990) .
(0.990) Según
(0.990) un
(0.990) fascinante
(0.990) estudio
(1.000) de
(0.990) investigación
(0.990) rea
(0.990) lizado
(1.000) en
(0.990) la
(0.990) Universidad
(1.000) de
(0.990) Gifu
(0.990) ,
(0.990) en
(0.990) Japón
(0.990) ,
(0.990) la
(0.990) masticación
(0.990) mejora
(0.990) la
(0.990) memoria
(0.990) al
(0.990) reducir
(0.990) la
(0.990) liberación
(1.000) de
(0.990) las
(0.990) hormonas
(0.990) del
(0.990) estrés
(0.990) .
(0.980) La
(0.990) técnica
(1.000) de
(0.990) formación
(0.990) de
(0.980) ima
(0.990) gen
(0.990) por
(0.990) resonancia
(0.990) magnética
(0.990) (
(0.990) IRM
(0.990) )
(0.990) muestra
(0.990) que
(0.990) la
(0.990) masticación
(0.990) estimula
(0.990) el
(0.990) hi
(0.990) pocampo
(0.990) ,
(0.990) el
(0.990) cual
(0.990) ,
(0.990) a
(0.990) su
(1.000) vez
(0.990) ,
(0.990) ayuda
(1.000) a
(0.990) controlar
(0.990) los
(0.990) niveles
(0.990) de
(0.990) hormonas
(0.990) del
(0.990) estrés
(0.990) en
(0.990) sangre
(0.990) .
(0.990) El
(0.980) resultado
(0.990) es
(0.990) que
(1.000) el
(0.990) simple
(0.990) acto
(0.990) de
(0.990) masticar
(0.990) reduce
(0.990) tanto
(0.990) el
(0.990) estrés
(0.990) como
(0.990) las
(0.990) hormonas
(0.990) del
(0.990) estrés
(0.990) ,
(0.970) de
(0.990) modo
(0.990) que
(0.990) masticar
(0.990) bien
(0.990) los
(0.990) alimentos
(0.990) puede
(0.990) reducir
(0.990) efectivamente
(0.990) el
(0.990) grado
(1.000) de
(0.990) ansiedad
(0.820) .

Los científicos japoneses descubrieron también que cuando faltan dientes o éstos se hallan en mal estado, se suele masticar menos. Ello hace que, acto seguido, aumenten los niveles de hormonas del estrés. La conclusión de este estudio es que una buena salud dental y una adecuada masticación son factores muy importantes para conservar la memoria cuando envejecemos y para protegernos de los dañinos efectos del estrés.

Paragraph confidence: 0.990
(0.990) Los
(0.990) científicos
(0.990) japoneses
(0.990) descubrieron
(0.990) también
(0.990) que
(0.990) cuando
(0.990) faltan
(0.990) dientes
(0.990) o
(0.960) és
(0.990) tos
(0.990) se
(0.990) hallan
(0.990) en
(0.990) mal
(0.990) estado
(0.990) ,
(0.990) se
(0.990) suele
(0.990) masticar
(0.990) menos
(0.990) .
(0.990) Ello
(0.990) hace
(0.990) que
(0.980) ,
(0.980) acto
(0.990) seguido
(0.980) ,
(0.990) aumenten
(0.990) los
(0.990) niveles
(1.000) de
(0.990) hormonas
(0.990) del
(0.990) estrés
(0.990) .
(0.990) La
(0.990) conclusión
(1.000) de
(0.990) este
(0.990) estudio
(0.990) es
(0.990) que
(0.990) una
(0.990) buena
(0.990) salud
(0.990) dental
(0.990) y
(0.990) una
(0.990) adecuada
(0.990) masticación
(0.990) son
(0.980) factores
(0.990) muy
(0.990) importantes
(0.990) para
(0.990) conservar
(0.990) la
(0.990) memoria
(0.990) cuando
(0.990) envejecemos
(0.990) y
(0.990) para
(0.990) protegernos
(0.990) de
(0.990) los
(0.990) dañinos
(0.990) efectos
(0.990) del
(0.990) estrés
(0.980) .

Una vez ha pasado por el esofago, el alimento entra en el estómago. Si lo que comemos contiene hidratos de carbono (azúcares complejos y almidones como los que

Paragraph confidence: 0.980
(0.990) Una
(0.990) vez
(0.970) ha
(0.990) pasado
(0.990) por
(1.000) el
(0.870) esofago
Possible mistake: symbol 'o' in word 'esofago' (confidence: 0.460)
(0.900) ,
(0.970) el
(0.990) alimento
(0.990) entra
(0.990) en
(0.990) el
(0.990) estómago
(0.990) .
(0.990) Si
(0.990) lo
(0.990) que
(0.990) co
(0.990) memos
(0.990) contiene
(0.990) hidratos
(0.990) de
(0.990) carbono
(0.950) (
(0.990) azúcares
(0.990) complejos
(0.990) y
(0.990) almidones
(0.990) como
(0.990) los
(0.990) que

Block confidence: 0.890

se encuent

Paragraph confidence: 0.890
(0.980) se
(0.860) encuent
Possible mistake: symbol 't' in word 'encuent' (confidence: 0.530)
```

### Alternative: Use <u>gcloud</u> command

To perform entity analysis, use the [`gcloud ml vision detect-text`](https://cloud.google.com/sdk/gcloud/reference/ml/vision/detect-text) command using the [Google Cloud SDK](https://cloud.google.com/sdk/docs/) as shown in the following example:

```shell
gcloud ml vision detect-text "gs://bucket-name-123/abbey_road.jpg"
```

![](https://cloud.google.com/vision/docs/images/abbey_road.png)

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
                      "x": 46,
                      "y": 43
                    },
                    {
                      "x": 268,
                      "y": 39
                    },
                    {
                      "x": 270,
                      "y": 131
                    },
                    {
                      "x": 48,
                      "y": 135
                    }
                  ]
                },
                "paragraphs": [
                  {
                    "boundingBox": {
                      "vertices": [
                        {
                          "x": 46,
                          "y": 43
                        },
                        {
                          "x": 268,
                          "y": 39
                        },
                        {
                          "x": 270,
                          "y": 131
                        },
                        {
                          "x": 48,
                          "y": 135
                        }
                      ]
                    },
                    "property": {
                      "detectedLanguages": [
                        {
                          "languageCode": "en"
                        }
                      ]
                    },
                    "words": [
                      {
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 46,
                              "y": 44
                            },
                            {
                              "x": 179,
                              "y": 41
                            },
                            {
                              "x": 180,
                              "y": 81
                            },
                            {
                              "x": 47,
                              "y": 84
                            }
                          ]
                        },
                        "property": {
                          "detectedLanguages": [
                            {
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
                                  "y": 44
                                },
                                {
                                  "x": 71,
                                  "y": 43
                                },
                                {
                                  "x": 72,
                                  "y": 83
                                },
                                {
                                  "x": 47,
                                  "y": 84
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "A"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 74,
                                  "y": 43
                                },
                                {
                                  "x": 100,
                                  "y": 42
                                },
                                {
                                  "x": 101,
                                  "y": 81
                                },
                                {
                                  "x": 75,
                                  "y": 82
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "B"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 101,
                                  "y": 43
                                },
                                {
                                  "x": 126,
                                  "y": 42
                                },
                                {
                                  "x": 127,
                                  "y": 81
                                },
                                {
                                  "x": 102,
                                  "y": 82
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "B"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 132,
                                  "y": 42
                                },
                                {
                                  "x": 152,
                                  "y": 42
                                },
                                {
                                  "x": 153,
                                  "y": 82
                                },
                                {
                                  "x": 133,
                                  "y": 82
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "E"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 156,
                                  "y": 42
                                },
                                {
                                  "x": 179,
                                  "y": 42
                                },
                                {
                                  "x": 180,
                                  "y": 82
                                },
                                {
                                  "x": 157,
                                  "y": 82
                                }
                              ]
                            },
                            "property": {
                              "detectedBreak": {
                                "type": "EOL_SURE_SPACE"
                              },
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "Y"
                          }
                        ]
                      },
                      {
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 47,
                              "y": 95
                            },
                            {
                              "x": 155,
                              "y": 94
                            },
                            {
                              "x": 155,
                              "y": 133
                            },
                            {
                              "x": 47,
                              "y": 134
                            }
                          ]
                        },
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "symbols": [
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 47,
                                  "y": 96
                                },
                                {
                                  "x": 68,
                                  "y": 96
                                },
                                {
                                  "x": 68,
                                  "y": 134
                                },
                                {
                                  "x": 47,
                                  "y": 134
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "R"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 74,
                                  "y": 95
                                },
                                {
                                  "x": 97,
                                  "y": 95
                                },
                                {
                                  "x": 97,
                                  "y": 134
                                },
                                {
                                  "x": 74,
                                  "y": 134
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "O"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 101,
                                  "y": 95
                                },
                                {
                                  "x": 126,
                                  "y": 95
                                },
                                {
                                  "x": 126,
                                  "y": 133
                                },
                                {
                                  "x": 101,
                                  "y": 133
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "A"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 131,
                                  "y": 94
                                },
                                {
                                  "x": 155,
                                  "y": 94
                                },
                                {
                                  "x": 155,
                                  "y": 133
                                },
                                {
                                  "x": 131,
                                  "y": 133
                                }
                              ]
                            },
                            "property": {
                              "detectedBreak": {
                                "type": "SPACE"
                              },
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
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
                              "y": 93
                            },
                            {
                              "x": 269,
                              "y": 92
                            },
                            {
                              "x": 269,
                              "y": 131
                            },
                            {
                              "x": 180,
                              "y": 132
                            }
                          ]
                        },
                        "property": {
                          "detectedLanguages": [
                            {
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
                                  "x": 205,
                                  "y": 93
                                },
                                {
                                  "x": 205,
                                  "y": 132
                                },
                                {
                                  "x": 180,
                                  "y": 132
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "N"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 211,
                                  "y": 93
                                },
                                {
                                  "x": 249,
                                  "y": 93
                                },
                                {
                                  "x": 249,
                                  "y": 131
                                },
                                {
                                  "x": 211,
                                  "y": 131
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
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
                                  "x": 269,
                                  "y": 92
                                },
                                {
                                  "x": 269,
                                  "y": 131
                                },
                                {
                                  "x": 248,
                                  "y": 131
                                }
                              ]
                            },
                            "property": {
                              "detectedBreak": {
                                "type": "EOL_SURE_SPACE"
                              },
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "8"
                          }
                        ]
                      }
                    ]
                  }
                ],
                "property": {
                  "detectedLanguages": [
                    {
                      "languageCode": "en"
                    }
                  ]
                }
              },
              {
                "blockType": "TEXT",
                "boundingBox": {
                  "vertices": [
                    {
                      "x": 50,
                      "y": 161
                    },
                    {
                      "x": 249,
                      "y": 158
                    },
                    {
                      "x": 249,
                      "y": 175
                    },
                    {
                      "x": 50,
                      "y": 178
                    }
                  ]
                },
                "paragraphs": [
                  {
                    "boundingBox": {
                      "vertices": [
                        {
                          "x": 50,
                          "y": 161
                        },
                        {
                          "x": 249,
                          "y": 158
                        },
                        {
                          "x": 249,
                          "y": 175
                        },
                        {
                          "x": 50,
                          "y": 178
                        }
                      ]
                    },
                    "property": {
                      "detectedLanguages": [
                        {
                          "languageCode": "en"
                        }
                      ]
                    },
                    "words": [
                      {
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 50,
                              "y": 161
                            },
                            {
                              "x": 85,
                              "y": 160
                            },
                            {
                              "x": 85,
                              "y": 176
                            },
                            {
                              "x": 50,
                              "y": 177
                            }
                          ]
                        },
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "symbols": [
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 50,
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
                                  "x": 50,
                                  "y": 177
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
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
                                  "y": 161
                                },
                                {
                                  "x": 67,
                                  "y": 161
                                },
                                {
                                  "x": 67,
                                  "y": 177
                                },
                                {
                                  "x": 60,
                                  "y": 177
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "I"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 68,
                                  "y": 161
                                },
                                {
                                  "x": 74,
                                  "y": 161
                                },
                                {
                                  "x": 74,
                                  "y": 177
                                },
                                {
                                  "x": 68,
                                  "y": 177
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "T"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 76,
                                  "y": 162
                                },
                                {
                                  "x": 85,
                                  "y": 162
                                },
                                {
                                  "x": 85,
                                  "y": 177
                                },
                                {
                                  "x": 76,
                                  "y": 177
                                }
                              ]
                            },
                            "property": {
                              "detectedBreak": {
                                "type": "SPACE"
                              },
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "Y"
                          }
                        ]
                      },
                      {
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 95,
                              "y": 161
                            },
                            {
                              "x": 114,
                              "y": 161
                            },
                            {
                              "x": 114,
                              "y": 177
                            },
                            {
                              "x": 95,
                              "y": 177
                            }
                          ]
                        },
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "symbols": [
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 95,
                                  "y": 161
                                },
                                {
                                  "x": 104,
                                  "y": 161
                                },
                                {
                                  "x": 104,
                                  "y": 177
                                },
                                {
                                  "x": 95,
                                  "y": 177
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "O"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 107,
                                  "y": 161
                                },
                                {
                                  "x": 114,
                                  "y": 161
                                },
                                {
                                  "x": 114,
                                  "y": 176
                                },
                                {
                                  "x": 107,
                                  "y": 176
                                }
                              ]
                            },
                            "property": {
                              "detectedBreak": {
                                "type": "SPACE"
                              },
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "F"
                          }
                        ]
                      },
                      {
                        "boundingBox": {
                          "vertices": [
                            {
                              "x": 122,
                              "y": 161
                            },
                            {
                              "x": 249,
                              "y": 159
                            },
                            {
                              "x": 249,
                              "y": 175
                            },
                            {
                              "x": 122,
                              "y": 177
                            }
                          ]
                        },
                        "property": {
                          "detectedLanguages": [
                            {
                              "languageCode": "en"
                            }
                          ]
                        },
                        "symbols": [
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 122,
                                  "y": 161
                                },
                                {
                                  "x": 138,
                                  "y": 161
                                },
                                {
                                  "x": 138,
                                  "y": 177
                                },
                                {
                                  "x": 122,
                                  "y": 177
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "W"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 141,
                                  "y": 161
                                },
                                {
                                  "x": 150,
                                  "y": 161
                                },
                                {
                                  "x": 150,
                                  "y": 177
                                },
                                {
                                  "x": 141,
                                  "y": 177
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "E"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 151,
                                  "y": 160
                                },
                                {
                                  "x": 160,
                                  "y": 160
                                },
                                {
                                  "x": 160,
                                  "y": 176
                                },
                                {
                                  "x": 151,
                                  "y": 176
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "S"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 161,
                                  "y": 160
                                },
                                {
                                  "x": 170,
                                  "y": 160
                                },
                                {
                                  "x": 170,
                                  "y": 176
                                },
                                {
                                  "x": 161,
                                  "y": 176
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
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
                                  "y": 160
                                },
                                {
                                  "x": 182,
                                  "y": 160
                                },
                                {
                                  "x": 182,
                                  "y": 176
                                },
                                {
                                  "x": 172,
                                  "y": 176
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "M"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 183,
                                  "y": 160
                                },
                                {
                                  "x": 192,
                                  "y": 160
                                },
                                {
                                  "x": 192,
                                  "y": 176
                                },
                                {
                                  "x": 183,
                                  "y": 176
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "I"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 196,
                                  "y": 160
                                },
                                {
                                  "x": 206,
                                  "y": 160
                                },
                                {
                                  "x": 206,
                                  "y": 175
                                },
                                {
                                  "x": 196,
                                  "y": 175
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
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
                                  "y": 160
                                },
                                {
                                  "x": 218,
                                  "y": 160
                                },
                                {
                                  "x": 218,
                                  "y": 175
                                },
                                {
                                  "x": 208,
                                  "y": 175
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "S"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 219,
                                  "y": 159
                                },
                                {
                                  "x": 229,
                                  "y": 159
                                },
                                {
                                  "x": 229,
                                  "y": 174
                                },
                                {
                                  "x": 219,
                                  "y": 174
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "T"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 231,
                                  "y": 159
                                },
                                {
                                  "x": 238,
                                  "y": 159
                                },
                                {
                                  "x": 238,
                                  "y": 174
                                },
                                {
                                  "x": 231,
                                  "y": 174
                                }
                              ]
                            },
                            "property": {
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "E"
                          },
                          {
                            "boundingBox": {
                              "vertices": [
                                {
                                  "x": 241,
                                  "y": 159
                                },
                                {
                                  "x": 249,
                                  "y": 159
                                },
                                {
                                  "x": 249,
                                  "y": 174
                                },
                                {
                                  "x": 241,
                                  "y": 174
                                }
                              ]
                            },
                            "property": {
                              "detectedBreak": {
                                "type": "EOL_SURE_SPACE"
                              },
                              "detectedLanguages": [
                                {
                                  "languageCode": "en"
                                }
                              ]
                            },
                            "text": "R"
                          }
                        ]
                      }
                    ]
                  }
                ],
                "property": {
                  "detectedLanguages": [
                    {
                      "languageCode": "en"
                    }
                  ]
                }
              }
            ],
            "height": 240,
            "property": {
              "detectedLanguages": [
                {
                  "languageCode": "en"
                }
              ]
            },
            "width": 320
          }
        ],
        "text": "ABBEY\nROAD NW8\nCITY OF WESTMINSTER\n"
      },
      "textAnnotations": [
        {
          "boundingPoly": {
            "vertices": [
              {
                "x": 46,
                "y": 41
              },
              {
                "x": 269,
                "y": 41
              },
              {
                "x": 269,
                "y": 177
              },
              {
                "x": 46,
                "y": 177
              }
            ]
          },
          "description": "ABBEY\nROAD NW8\nCITY OF WESTMINSTER\n",
          "locale": "en"
        },
        {
          "boundingPoly": {
            "vertices": [
              {
                "x": 46,
                "y": 44
              },
              {
                "x": 179,
                "y": 41
              },
              {
                "x": 180,
                "y": 81
              },
              {
                "x": 47,
                "y": 84
              }
            ]
          },
          "description": "ABBEY"
        },
        {
          "boundingPoly": {
            "vertices": [
              {
                "x": 47,
                "y": 95
              },
              {
                "x": 155,
                "y": 94
              },
              {
                "x": 155,
                "y": 133
              },
              {
                "x": 47,
                "y": 134
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
                "y": 93
              },
              {
                "x": 269,
                "y": 92
              },
              {
                "x": 269,
                "y": 131
              },
              {
                "x": 180,
                "y": 132
              }
            ]
          },
          "description": "NW8"
        },
        {
          "boundingPoly": {
            "vertices": [
              {
                "x": 50,
                "y": 161
              },
              {
                "x": 85,
                "y": 160
              },
              {
                "x": 85,
                "y": 176
              },
              {
                "x": 50,
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
                "x": 95,
                "y": 161
              },
              {
                "x": 114,
                "y": 161
              },
              {
                "x": 114,
                "y": 177
              },
              {
                "x": 95,
                "y": 177
              }
            ]
          },
          "description": "OF"
        },
        {
          "boundingPoly": {
            "vertices": [
              {
                "x": 122,
                "y": 161
              },
              {
                "x": 249,
                "y": 159
              },
              {
                "x": 249,
                "y": 175
              },
              {
                "x": 122,
                "y": 177
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