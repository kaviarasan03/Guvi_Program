n1=int(input())
li=list(map(int,input().split()))
li1=[]
for i in range(0,len(li)):
    if i==li[i]:
        li1.append(li[i])
if len(li1)>0:
    print(*li1)
else:
    print("-1")
        
        
