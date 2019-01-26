n1=int(input())
li=list(map(int,input().split()))
li.sort()
li1=[]
for i in range(0,len(li)-1):
    if li[i]==li[i+1]:
        if li[i] not in li1:
            li1.append(li[i])
li1.sort()
if len(li1)>0:
    print(*li1)
else:
    print("unique")
 
    
        
