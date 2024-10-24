import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def read_corpus(filepath='corpus.txt'):
    with open(filepath, 'r') as f:
        corpus = f.read().lower()
        return remove_punctuation(corpus).split()

def count_token_occurrences(corpus, token):
    return corpus.count(token.lower())