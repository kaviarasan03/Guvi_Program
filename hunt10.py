n,n2=map(int,input().split( ))
l1=list(map(int,input().split( )))
l2=list(map(int,input().split( )))
c=0
for i in l2:
    
    if i in l1:
        c=c+1
if c==len(l2):
    print("YES")
else:
    print("NO")
    
