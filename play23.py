n1,k=map(int,input().split( ))
li1=list(map(int,input().split( )))
li2=list(map(int,input().split( )))
m1=max(li1)
m2=max(li2)
li3=[]
li3.append(m1)
for i in range(0,k-1):
    li3.append(m2)
print(*li3)    
