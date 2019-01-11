n1=int(input())
s=str(n1)
c=0
l=len(s)
for i in s:
    if i=="0" or i=="1":
        c=c+1
	
if c==l:
    print("yes")
else:
    print("no")
