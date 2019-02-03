n1=input()
flag=0
li=[]
for i in n1:
    if i!=" ":
        li.append(i)
        flag=0
    elif i==" " and flag==0:
        li.append(i)
        flag=1
    elif i==" " and flag==1:
        pass
for i in li:
    print(i,end='')
        
        
