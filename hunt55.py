n1,k=map(int,input().split( ))
li=list(map(int,input().split( )))

for i in range(0,k):
    a=li[0]
    li.remove(a)
    li.append(a)
print(*li)    

