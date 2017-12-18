a=[]
for lis in range(int(input())):
    name = input()
    score = float(input())
    a.append( [name,score])

    
print (a)
b=[]
for x in a:
    b.append(x[1])
print(b)
def minimum1(arr,size):
    val=0
    x=min(arr)
    c=0
    for i in range (0,size):
        c=c+1
        if arr[i] == x:
            val=arr[i]
            b.pop(i)
            break;
            

    return val

size=len(b)
val1=minimum1(b,size)

size=len(b)

val2=minimum1(b,size)
for x in a:
    if x[1]==val1: 
        print (x[0])

for x in a:
    if x[1]==val2:
        print(x[0])
    
