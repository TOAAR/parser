import nltk
#nltk.download('averaged_perceptron_tagger')
#nltk.download('averaged_perceptron_tagger_eng')


from nltk.tokenize import TreebankWordTokenizer


def extract_noun_phrases(text):
    tokenizer = TreebankWordTokenizer()
    words = tokenizer.tokenize(text)
    tagged = nltk.pos_tag(words)

    grammar = "NP: {<DT>?<JJ.*>*<NN.*>+}"
    cp = nltk.RegexpParser(grammar)
    tree = cp.parse(tagged)

    print("\nParsed Tree:")
    tree.pretty_print()

    print("\nNoun Phrase Chunks:")
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            np = " ".join(word for word, tag in subtree.leaves())
            print(np)

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    extract_noun_phrases(sentence)
