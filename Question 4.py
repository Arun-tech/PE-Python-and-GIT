n=int(input("Enter number of pairs"))

Dict={}
Dict[0]=[]
x=0

def verify(a,b):
    if (a in Dict[b]):
        return True
    return False

for i in range(n):
    string=input("Enter the pairs as strings seperated by space ")
    List=string.split()
    temp=0
    for j in range(x+1):
        if verify(List[0],j) or verify(List[1],j):
            if(verify(List[0],j)):
                Dict[j]=Dict[j]+[List[1]]
            else:
                Dict[j]=Dict[j]+[List[0]]
            temp=1
            break

    if temp==0:
        if i!=0:
            x=x+1
        else:
            x=0
        Dict[x]=[]
        print(Dict)
        Dict[x]=Dict[x] + List

print(Dict)

print("There are"+str(len(Dict))+" groups")

string=input("Enter the pairs as strings seperated by space ")
List=string.split()
temp=0
for j in range(x+1):
    if verify(List[0],j) and verify(List[1],j):
        temp=1
        break

if(temp==1):
    print(List[0]+", "+List[1]+" belongs to the same group")
else:
    print(List[0]+", "+List[1]+" do not belong to the same group")
