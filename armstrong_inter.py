n1,n3=map(int,input().split( ))
li=[]
for i in range(n1+1,n3):
	n=i
	sum1=0
	
	while n>0:
	    r=n%10
	    n=n//10
	    r=r*r*r
	    sum1=sum1+r
	if i==sum1:
		li.append(sum1)	
print(*li)
	
