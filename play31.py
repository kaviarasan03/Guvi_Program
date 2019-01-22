n1=input()
a=b=0
for i in n1:
    if i=="(":
        a+=1
    elif i==")":
        b+=1
if a==b:
    print("yes")
else:
    print("no")
