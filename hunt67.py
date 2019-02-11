n1=input()
n2=input()
li1=[]
li2=[]
for i in range(0,len(n1)-1):
	
	if n1[i]=='#':
		li1.append(n1[i+1])
m1=max(li1)
		
for i in range(0,len(n2)-1):
	
	if n2[i]=='#':
		li2.append(n2[i+1])
n=max(li2)
if m1<n:
	for i in n2:
		if i=='#':
			break
		else:
			print(i,end='')
else:
	for i in n1:
		if i=='#':
			break
		else:
			print(i,end='')
				
