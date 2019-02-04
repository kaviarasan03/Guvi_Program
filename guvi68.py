n1=int(input())
li=list(map(int,input().split( )))
a=max(li)
b=min(li)
for i in range(0,n1):
	if li[i]==a:
		c=i+1
	if li[i]==b:
		d=i+1
print(d,c)		
