
def bigram(word):
    gram = []
    for i in range(len(word) - 1):
        gram.append(word[i] + word[i + 1])
    return gram

def trigram(word):
    gram = []
    for i in range(len(word) - 2):
        gram.append(word[i] + word[i + 1] + word[i + 2])
    return gram
