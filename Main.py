import fileManager
import Test
from timeit import default_timer as timer

#fileManager.nGramPopulate()
query = input("Insert name: ")
distance = input("Insert the max distance: ")
n = input("Insert dimension of grams: ")

start=timer()
editList=Test.testEdit(query,distance)
end=timer()
print("Only EditDistance: ",end-start)
print(editList)

start=timer()
ngramList=Test.testNgram(query,distance,n)
end=timer()
print("EditDistance and n-grams: ",end-start)
print(ngramList)