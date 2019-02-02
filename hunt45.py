n1=int(input())
li=list(map(int,input().split( )))
c=0
for i in range(1,n1+1):
    a=n1*i
    if a in li:
        c=c+1
print(c)        
        
