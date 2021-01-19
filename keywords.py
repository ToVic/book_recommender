import spacy
from string import punctuation
nlp = spacy.load("en_core_web_lg")

def extract_keywords(input_question, num_tags=None):
    kw_list = []
    type_tag = ['ADJ','NOUN','PROPN']
    doc = nlp(input_question.lower())
    for token in doc:
        if (token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if (token.pos_ in type_tag):
            kw_list.append(token.text)
    #tweak the following to return most important keywords, not just first X keywords
    if num_tags:
        return kw_list[:num_tags]
    else:
        return kw_list
