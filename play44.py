s,n=input().split( )
s=str(s)
n=int(n)
s1=s[::-1]
l=list(s1)
for i in range(0,n):
    a=l[0]
    l.remove(a)
    l.append(a)
for j in range(len(l)-1,-1,-1):
    print(l[j],end='')

