
n1,k=map(int,input().split( ))
li=list(map(int,input().split( )))

for i in range(0,len(li)):
    if i==k:
        print(li[i-1])    
    
