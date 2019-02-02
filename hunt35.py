n1=input()
l=len(n1)
d=int(l/2)
a=n1[0:d]
b=n1[d+1:l]
if a==b:
    print("YES")
else:
    print("NO")
