n1=input().split( )
li=[]
for i in range(0,len(n1)):
    a=n1[i][::-1]
    li.append(a)
print(*li)    
