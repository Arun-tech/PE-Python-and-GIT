#Question 3 final

lex=list()
x=str(input("enter the lexiographic order as a single word")) #x takes the order as a single word
for i in x:
    lex.append(i)        #the order is stored as a list in lex
    
string=list()
n=int(input("Enter number of words "))   #n takes number of words
for i in range(0,n):
    k=str(input("Enter a word"))
    string.append(k)                    #inputting the words into "string" as elements of list
string2=list()
string=sorted(string)                  #"string" is now sorted


for i in lex:                          #iterating through the list that has lexicographic order
    for j in string:                   #iterating through sorted list "string"
        if(j[0]==i):                   #checking if first letter of j is same as i   
            if j not in string2:    
                string2.append(j)      #if true, then the word gets appended to "string2"
print("\nNew Lexicographic order : ",lex[:])          #to print the lexicographic order
print("\nLexicographically sorted list :\n",string2)  #to print the words in lexicographical order
                



