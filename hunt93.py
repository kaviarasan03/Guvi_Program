s1=input()
c=0
li=[]
for i in s1:
    if i!=" ":
        c=c+1
        if c%2==1:
            li.append(i.upper())
        else:
            li.append(i)
    else:
        li.append(i)
for i in li:
    print(i,end='')
            
