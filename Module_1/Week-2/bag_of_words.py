def tokenization(dataset: list[str], string: str):
    """Bag of Words (NLP) is an algorithm to help
    process natural language and classify text. 
    For each new test data, find the number of words 
    in the text.
    """
    # read dataset and turn into tokens
    token: dict = {}
    for text in dataset:
        for word in text.split():
            if word not in token:
                token[word] = 0

    # read string
    for word in string.split():
        if word in token:
            token[word] += 1

    # get input:
    vector: list[str] = []
    vector_binary: list[int] = []
    for key, value in token.items():
        vector.append(key)
        vector_binary.append(value)

    print(f'Token of "{string}": {vector_binary}')
    print(f'Bag of Words: {vector}')


def main():
    corpus: list[str] = ['I love Maths lesson',
                         'I love AI', 'I love music lessons']
    text: str = 'I love AI love Maths'
    tokenization(dataset=corpus, string=text)


if __name__ == '__main__':
    main()
