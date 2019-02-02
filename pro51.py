n=int(input())
li=list(map(int,input().split( )))
c=1
li1=[]

for i in range(0,n):
    if n==1:
        li.append(c)
    else:    
        for j in range(i+1,n):
            
            if li[i]>0 and li[j]<0:
                
                c=c+1
                    
                
            elif li[i]<0 and li[j]>0:
                
                c=c+1
            else:
                li.append(c)
                break
                    
                    
              
            

                
            i=i+1
            
        li1.append(c)
        c=1
print(*li1)        
