from nltk.tokenize import RegexpTokenizer

def word_tokenize(text):
    tokenize = RegexpTokenizer("[\w`'‘‘‘’‘-]+")
    tokens = tokenize.tokenize(text)
    return tokens
