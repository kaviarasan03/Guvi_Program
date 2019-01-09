n1,n2=map(int,input().split( ))
li=[]
for j in range(n1+1,n2):
	if j%2==1:
		li.append(j)
for i in range(len(li)-1):
    print(li[i],end=" ")
print(li[len(li)-1]) 		
	
