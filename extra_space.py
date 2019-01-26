n1=input()
flag=1
li=[]
for i in n1:
    if i!=" ":
        li.append(i)
        flag=1
    elif i==" " and flag==1:
        li.append(i)
        flag=0
for i in li:
    print(i,end='')
        
        
        
