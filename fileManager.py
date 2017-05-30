import divide
import string

def nGramPopulate():
    #alphabet=__import__("string").lowercase

    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            open("C:\\Users\\Luca\\PycharmProjects\\ngramEditDistance\\2gram\\"+i+j+"-gram.txt","w")

    names = open("C:\\Users\\Luca\\PycharmProjects\\ngramEditDistance\\nomi.txt", "r")
    for k in names:
        name=k[:len(k)-1]
        if(name == 'ï»¿abaco'):
            name='abaco'
        gram = divide.bigram(name)
        for z in gram:
            fileName="C:\\Users\\Luca\\PycharmProjects\\ngramEditDistance\\2gram\\"+z+"-gram.txt"
            f = open(fileName, "a")
            f.write(name+"\n")

    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            for k in string.ascii_lowercase:
                #fileName=i+j+k+".txt"
                open("C:\\Users\\Luca\\PycharmProjects\\ngramEditDistance\\3gram\\"+i+j+k+"-gram.txt","w")

    names = open("C:\\Users\\Luca\\PycharmProjects\\ngramEditDistance\\nomi.txt", "r")
    for k in names:
        name=k[:len(k)-1]
        if(name == 'ï»¿abaco'):
            name='abaco'
        gram = divide.trigram(name)
        for z in gram:
            fileName="C:\\Users\\Luca\\PycharmProjects\\ngramEditDistance\\3gram\\"+z+"-gram.txt"
            f = open(fileName, "a")
            f.write(name+"\n")