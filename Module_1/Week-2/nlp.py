from bag_of_words import tokenization


def nlp(dataset, stop_words, text):
    # clear stop words from text
    new_text: str = ""
    for word in text.split():
        if word not in stop_words:
            new_text = new_text + ' ' + word

    tokenization(dataset=dataset, string=new_text)


def main():
    corpus: list[str] = ['I love Maths lessons',
                         'I love AI', 'I love listen to music']
    stop_words: list[str] = ['I', 'love', 'and', 'to']
    text: str = 'I love AI and listen to music'
    nlp(dataset=corpus, stop_words=stop_words, text=text)


if __name__ == '__main__':
    main()
