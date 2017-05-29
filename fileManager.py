import divide
import string

def nGramPopulate():
    #alphabet=__import__("string").lowercase
    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            fileName=i+j+".txt"
            open(fileName,"w")

    names = open("C:\\Users\\Luca\\PycharmProjects\\ngramEditDistance\\nomi.txt", "r")
    for k in names:
        # Se k contiene il bigramma i+j allora scrivilo nel file appena creato
        name=k[:len(k)-1]
        if(name == 'ï»¿abaco'):
            name='abaco'
        gram = divide.bigram(name)
        for z in gram:
            fileName=z+".txt"
            f = open(fileName, "a")
            f.write(name+"\n")
