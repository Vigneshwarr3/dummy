from dummy import read_corpus, count_token_occurrences

def report_count(token):
    corpus = read_corpus(filepath)
    count = count_token_occurrences(corpus, token)
    print(f"The term [{token}] shows up in the corpus {count} times.")