def report_count(token):
    try:
        with open('corpus.txt', 'r') as file:
            corpus = file.read()

        count = corpus.lower().split().count(token.lower())

        print(f"The term {token} shows up in the corpus {count} times.")
    
    except FileNotFoundError:
        print("The corpus.txt file was not found.")