n1=int(input())
li=list(map(int,input().split( )))
li1=[]
for i in range(0,len(li)):
    a=li[0]
    li1.append(a)
    if i!=0:
        if a in li1:
            print(a)
            break
    li.remove(a)
    li.append(a)
else:
    print("unique")
