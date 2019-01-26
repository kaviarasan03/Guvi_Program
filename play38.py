n1=int(input())
li=[]
for i in range(2,n1+1):
    if n1%i==0:
        if i%2==0:
            li.append(i)
print(*li)            
