#Question 1

def Binarysearch(array,x,y,z):
    if (y>1):
        centre=int((x+(y-1))/2)

        if (array[centre]==z):
            return centre

        elif(int(array[centre])>int(z)):
            return Binarysearch(array,x,centre-1,int(z))

        elif(int(array[centre])<int(z)):
            return Binarysearch(array,centre+1,y,int(z))

    else:
        return -1
            

array=list()
n=int(input("Enter number of elements "))
k=0
for i in range(0,n):
    k=input("Enter the element ")
    array.append(k)

a=int(input("Enter the element to be searched "))

result=Binarysearch(array,0,n-1,a)
if (result==-1):
    print("Element not found in the list")
else:
    print(result)

print(array[:])
