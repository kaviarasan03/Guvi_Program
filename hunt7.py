n1=int(input())
li=list(map(int,input().split( )))
li1=[]
for i in range(0,len(li)):
    if li[i]%2==1 and i%2==0:
        li1.append(li[i])
    elif li[i]%2==0 and i%2==1:
        li1.append(li[i])
print(*li1)        
        
