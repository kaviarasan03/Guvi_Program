n1,n2=map(int,input().split( ))
li=list(map(int,input().split( )))
li1=[]
li2=[]
c=0
k1=0

if n1==n2:
    print(min(li))
else:
    for i in range(0,n1):
        c=c+1
        k1=k1+1
        if c>n2:
            a=min(li1)
            li1=[]
            li2.append(a)
            li1.append(li[i])
            c=1
            
        
        else:
            li1.append(li[i])
        if k1==n1:
            b=min(li1)
            li2.append(b)
        
    f=max(li2)
    if f<0:
        print(min(li2))
    else:
        print(f)

