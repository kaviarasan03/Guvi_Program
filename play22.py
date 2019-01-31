n1=int(input())
li=list(map(int,input().split( )))
c=1
li1=[]
for i in li:
	c=c*i
	
for i in range(0,n):
	a=c//li[i]
	li1.append(a)
print(*li1)	
