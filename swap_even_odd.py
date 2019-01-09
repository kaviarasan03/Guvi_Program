st=input()
l=list(st)
for i in range(0,len(st),2):
    l[i],l[i+1]=l[i+1],l[i]
for i in range(len(l)-1):
    print(l[i],end="")
print(l[len(l)-1])     
    
