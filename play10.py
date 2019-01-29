n1,n2=map(str,input().split( ))
c1=0
for i in range(0,len(n1)):
    if n1[i]!=n2[i]:
	    c1+=1
if c1!=1:
	print("no")
else:
	print("yes")
 
