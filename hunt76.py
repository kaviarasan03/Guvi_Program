n=int(input())
li1=[]
for i in range(n):
	li=list(map(int,input().split( )))
	s=sum(li)
	print(s)
	li1.append(s)
a=sum(li1)
b1=a/(n*n)
print('%.6f' % b1)	
