n1=int(input())
li=list(map(int,input().split( )))
li1=[]
li2=[]
for i in li:
    li1.append(i)
    a=min(li1)
    li2.append(a)
print(*li2)    
