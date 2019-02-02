n1=int(input())
li=list(map(int,input().split( )))
l2=[]
for i in li:
    a=n1*i
    if a in li:
        l2.append(i)
if len(l2)!=0:
    print(*l2)
else:
    print("0")
    
