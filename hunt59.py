n1=int(input())
li1=list(map(int,input().split( )))
li2=list(map(int,input().split( )))
li3=[]
for i in range(0,n1):
    a=li1[i]+li2[i]
    li3.append(a)
print(*li3)    
   
