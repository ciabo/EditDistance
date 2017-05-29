import editD
import divide


def testEdit():
    query = input("Insert name: ")
    names = open("C:\\Users\\Luca\\PycharmProjects\\ngramEditDistance\\nomi.txt", "r")
    value = []
    query += "\n"
    for i in names:
        m = editD.editDistance(query, i)
        if m <= 1:
            value.append(i)
    print(value)


def testNgram():
    nGramQuery = []
    query = input("Insert name: ")
    n = input("Insert dimension of grams: ")
    distance = input("Insert the max distance: ")
    #Divide name in ngrams
    if int(n)==2:
        nGramQuery=divide.bigram(query)
        print(nGramQuery)
    if int(n)==3:
        nGramQuery=divide.trigram(query)

    for gram in nGramQuery:
        words=open("C:\\Users\\Luca\\PycharmProjects\\ngramEditDistance\\"+gram+".txt", "r")
        list=[]
        for w in words:
            name=w[:len(w)-1]
            editDistance=editD.editDistance(query,name)
            if(editDistance<=int(distance)):
                list.append(name)
    for element in list:
        print(element)
