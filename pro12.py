n1,q=map(int,input().split( ))
li=list(map(int,input().split( )))
for i in range(q):
	u,v=map(int,input().split( ))
	c=0
	for j in range(u-1,v):
		c=c+li[j]
	
	print(c)
