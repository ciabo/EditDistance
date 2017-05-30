import editD
import divide


def testEdit(query, distance):
    names = open("C:\\Users\\Luca\\PycharmProjects\\ngramEditDistance\\nomi.txt", "r")
    list = []
    for i in names:
        name=i[:len(i)-1]
        m = editD.editDistance(query, name)
        if m <= int(distance):
            list.append(name)
    return list


def testNgram(query, distance, n):
    nGramQuery = []
    #Divide name in ngrams
    if int(n)==2:
        nGramQuery=divide.bigram(query)
    if int(n)==3:
        nGramQuery=divide.trigram(query)

    list = []
    for gram in nGramQuery:
        if int(n)==2:
            words=open("C:\\Users\\Luca\\PycharmProjects\\ngramEditDistance\\2gram\\"+gram+"-gram.txt", "r")
        else:
            words = open("C:\\Users\\Luca\\PycharmProjects\\ngramEditDistance\\3gram\\" + gram + "-gram.txt", "r")

        for w in words:
            name=w[:len(w)-1]
            editDistance=editD.editDistance(query,name)
            if(editDistance<=int(distance)):
                if name not in list:
                    list.append(name)
    return list
