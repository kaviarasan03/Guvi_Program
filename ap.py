

n1,a,d=map(int,input().split())
i=a
x=[]
x.append(i)
c=1
while  c<n1:
    i=i+d
    x.append(i)
    c=c+1
print(sum(x))
