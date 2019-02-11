n1=int(input())
li=list(map(str,input().split( )))
k=input()
l=len(k)
c=0
for i in range(0,n1):
	a=li[i]
	b=a[0:l]
	if k==b:
		c=c+1
	a=''
print(c)	
