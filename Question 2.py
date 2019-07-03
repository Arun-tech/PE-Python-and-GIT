#Question2

Tuples=list()
n=int(input("Enter number of tuples you wish to enter "))
k=tuple()                         #k is declared as a Tuple
last=list()                       #last is a list of last elemnts of each tuple
for i in range(0,n):
    k=input("Enter the tuple ")   #k takes each tuple
    Tuples.append(k)              #k is appended to the list "Tuples"
    last.append(k[-2])            #last element of each tuple is appended to list "last" 

last.sort()                       #last is sorted in ascending order

Sorted=list()                     #Sorted will have elements of Tuples, but in sorted manner

for i in last:
    for j in Tuples:
        if(i==j[-2]):
            Sorted.append(j)     #Tuples are entered in "Sorted" in a sorted manner

print("\nSorted list of tuples as follows: ")
for i in range(0,len(Sorted)):
    print(i+1,".",Sorted[i])     #printing the sorted list of tuples
