n1,n2=map(int,input().split( ))
li=list(map(int,input().split( )))
c=0
for i in li:
    if i==n2:
        c=c+1
        break
    else:
        c=0
if c==1:
    print("yes")
else:
    print("no")
        
