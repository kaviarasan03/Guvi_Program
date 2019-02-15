n=int(input())
li=list(map(int,input().split( )))
m1=max(li)
li2=[]
for i in range(0,n-1):
	c=0
	for j in range(i+1,n):
		
		if li[i]>li[j]:
			c=c+1
	if c==(n-1-i):
		li2.append(li[i])
li2.append(li[n-1])		
print(*li2)
print(m1)
