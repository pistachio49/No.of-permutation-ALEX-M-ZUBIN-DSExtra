#We can do this problem in another way too:)
#This is done by making use of an inbuilt library in python known as itertools
#It contains many modules including permutations which generates all possible arrangements of elements in a list
#all the generated arrangements will be stored in a tuple

#for example
"""
#For the given code
 from itertools import permutations
 print list(permutations('sit',2)) --->it takes 2 parameters here,the string and the length of each arrangement we want
we get the output as shown below
 [('s', 'i'), ('s', 't'), ('i', 's'), ('i', 't'), ('t', 's'), ('t', 'i')]
i.e we get the output in a tuple
"""

#Main code
from itertools import permutations
I = raw_input().split() #input is taken as a string and a number separated by a space(eg-> sit 2)
k = map(''.join,list(permutations(I[0],int(I[1]))))

#map(function,iter) is another useful function in python which applies a given function to each element in the iterable (list, tuple etc.) 
#here each element in the tuple will be joined together by calling the map function
#i.e the elements in the above example([('s', 'i'), ('s', 't'), ('i', 's'), ('i', 't'), ('t', 's'), ('t', 'i')])
#will change to ['si', 'st', 'is', 'it', 'ts', 'ti'] 

for i in k:
    print ''.join(i) #printing each element 
