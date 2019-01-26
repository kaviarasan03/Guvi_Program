n1=int(input())
li=list(map(int,input().split( )))
li1=tuple(li)
li.sort()
c=0
for i in range(0,len(li)):

    if li1[i]==li[i]:
        c=c+1
if c==len(li):
    print("yes")
else:
    print("no")

