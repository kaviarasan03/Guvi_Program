s1=input()
li=[]
li1=[]
for i in s1:
    li.append(i)
for i in range(len(li),0,-1):
    a=li[i-1]
    li1.append(a)
if li==li1:
    print("Yes")
else:
    print("NO")
    
    
