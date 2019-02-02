n1=int(input())
li=list(map(int,input().split( )))

c=1
for i in li:
    c=c*i

if c<0:
    print(c*(-1))
else:
    print(c)
