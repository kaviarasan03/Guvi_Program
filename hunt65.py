n1,k=map(int,input().split( ))
li=list(map(int,input().split( )))
for i in range(0,n1):
	if k in li:
		li.remove(k)
if len(li)==0:
	print("empty")
else:
	print(*li)	
