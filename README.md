# multilang-ner-system-spacy

## Build

To build an app as Docker container, run `make build` (make sure, you have `Makefile` installed)

## Launch

To launch docker container, run `make launch-cpu`. This command opens command line inside the container.

## Run app

```
python app.py --input_text "{YOUR INPUT TEXT}" --language_code "{YOUR LANG CODE}"
```

Some tests are available as `test.sh` bash script.

## Limitations

App does not support all languages. In the case of missing language model, you will see the error

✘ No compatible package found for 'some_code_core_news_sm' (spaCy
v3.3.1)

and the app will load universal Mulitilang model `xx_ent_wiki_sm`
