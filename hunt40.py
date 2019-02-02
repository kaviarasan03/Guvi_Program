n=int(input())

s=str(n)
li=list(s)
c=0

for i in li:

    c=c+int(i)
c1=str(c)
c3=c1[::-1]
if len(c1)==1:
    print("YES")
elif c3==c1:
    print("YES")
else:
    print("NO")
    
