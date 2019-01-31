n1,k=map(int,input().split( ))
li=list(map(int,input().split( )))
c=0
for i in range(0,n1-1):
	for j in range(i+1,n1):
		if li[i]+li[j]==k:
			print("YES")
			c=c+1	
	break
if c!=1:
	print("NO")
			
