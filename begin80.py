n=input()
l=[]
for i in range(0,len(n),):
    if int(n[i])%2==1:
        
        l.append(n[i])
print(*l)    
