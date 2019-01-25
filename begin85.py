n1=input()
l1=[]
l2=[]
for i in range(0,len(n1)):
	if i%2!=0:
		l1.append(n1[i])
	else:
		l2.append(n1[i])
ls1=''.join(l1)
ls2=''.join(l2)
print(ls2,ls1)
 
