n1=int(input())
li=list(map(int,input().split( )))

li1=[]
for i in range(0,n1):
	if (n1-1)==i:
		c=0
		li1.append(c)
		break
	else:
		a=li[0]
		li.remove(a)
		b=max(li)
		li1.append(b)
print(*li1)		
	
