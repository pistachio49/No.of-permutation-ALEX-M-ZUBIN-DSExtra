#Program to generate all possible 'r' length strings from a given string of distinct elements

#The function permutation prints all possible arrangements of a string
#This function takes 3 parameters-
#* list b that contains the string
#* starting index of b(l)
#* ending index of b(r)

def permutation(b, l, r): 
    if l==r: 
        print ''.join(b) #printing the joined elements
        return
    else: 
        for i in xrange(l,r+1):
            b[l], b[i] = b[i], b[l] 
            permutation(b, l+1, r)  #recursive calling,
            b[l], b[i] = b[i], b[l] #backtracking

#Here, we fix an element, find the arrangements and then go back to it recursively
#this is for finding the further combinations available and this is called backtracking


#The function combination that generates all r combinations of a string
#This function takes 6 parameters-
#* the original list a,temporary list b,
#* start and end which points to the indices of list a,
#* index which points to b and the number r

def combination(a,b,start,end,index,r):
    if(index==r): #we get the current combination here  #i.e each time the list b is full we enter the if statement
        permutation(b,0,r-1) #the function permutation prints all the possible permutations of the list b
        return
    
    #we replace index with all possible elements
    #elements are fixed one by one and then recur for remaining indices
    #for eg, if the string we have is ABC and r is 2,
    #we first fix A and find all the combinations then fix B and so on
    i=start
    while(i<=end):
        b[index]=a[i]
        combination(a,b,i+1,end,index+1,r) #recursive calling of the function combination
        i+=1


#Driver code
string=raw_input("")  #taking the required string as the input
a = string.split()    #splitting the string
n = len(a) 
r=int(raw_input(""))  #reading r

b=[0]*r  #an empty list to store the elements initialised with zero
combination(a,b,0,n-1,0,r)

"""method of input/output(example)
-input format
A B C
2

-output
AB
BA
AC
CA
BC
CB
"""

