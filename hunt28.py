n1=input()
li=[]
for i in n1:
    if i not in li:
        li.append(i)
for i in li:
    print(i,end='')
