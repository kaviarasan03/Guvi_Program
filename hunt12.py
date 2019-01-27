n,n2=map(int,input().split( ))
li=list(map(int,input().split( )))
li.sort(reverse=True)
for i in range(0,n2-1):
    a=li[0]
    
        

    li.remove(a)
    if a==li[0]:
        
        li.remove(a)
print(li[0])    
