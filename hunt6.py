n1=int(input())
li=list(map(int,input().split( )))
li1=[]
for i in range(0,len(li)):
    a=li[0]
    li1.append(a)
    li.remove(a)
    if i!=0:
        if a in li1 and a in li:
            print(a)
            break
    
    li.append(a)
else:
    print("unique")
