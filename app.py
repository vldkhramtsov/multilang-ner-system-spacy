import argparse
from codecs import ignore_errors
import spacy

MULTILANGUAGE_UNIVERSAL_MODEL = "xx_ent_wiki_sm"


def parse_args():
    parser = argparse.ArgumentParser(description="Multi-lingual NER system.")
    parser.add_argument(
        "--input_text", required=True, type=str, help="Input text string for NER"
    )
    parser.add_argument(
        "--language_code",
        required=True,
        help="One of https://spacy.io/usage/models#languages",
    )
    return parser.parse_args()


def load_model(model: str):
    """
    Load model. If model is not loaded, download it and load
    """
    try:
        nlp = spacy.load(model)
    except OSError:
        spacy.cli.download(model)
        nlp = spacy.load(model)
    return nlp


def tag_entities(text: str, lang_code: str):
    model = f"{lang_code}_core_news_sm"
    try:
        nlp = load_model(model)
    # except Exception as e:
    except:
        # using bare except for pip errors of model download
        print(f"No {model} available. Loading {MULTILANGUAGE_UNIVERSAL_MODEL}")
        nlp = load_model(MULTILANGUAGE_UNIVERSAL_MODEL)

    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append(
            {
                "text": ent.text,
                "type": ent.label_,
                "start_pos": ent.start_char,
                "end_pos": ent.end_char,
            }
        )
    return entities


if __name__ == "__main__":
    args = parse_args()
    text = args.input_text
    lang_code = args.language_code
    entities = tag_entities(text, lang_code)
    print(entities)
