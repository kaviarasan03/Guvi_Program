n1=input()
li=[]
for i in n1:
    a=ord(i)
    b=a+3
    if b>90:
        b=b-26
    li.append(chr(b))
for i in li:
    print(i,end="")
    
    
