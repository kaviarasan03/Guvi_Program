n1,k=map(int,input().split( ))
li=list(map(int,input().split( )))
li1=[]
c=0
for i in range(0,n1-1):
    for j in range(i+1,n1):
        if abs(li[i]-li[j])==k:
            c=c+1
print(c)            
