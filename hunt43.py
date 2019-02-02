n=input()
li=list(n)
l1=[]
l2=[]
l3=[]
s=""
flag=0
for i in range(0,len(li)):

    if li[i].isalpha():
        l1.append(li[i])
        flag=0
    elif li[i].isnumeric() and flag==0:
        l2.append(li[i])
        flag=1
        t=li[i]
    elif li[i].isnumeric() and flag==1:
        v=t+li[i]
        del l2[len(l2)-1]
        
        l2.append(v)
        flag=1
       
for i in range(0,len(l2)):
    if int(l2[i])%2!=0:
        l3.append(l1[i])
        l3.append(l2[i])
    else:
        a=int(l2[i])
        l3.append(l1[i]*a)
for j in l3:
    s=s+j
print(s)    
        
        
    
