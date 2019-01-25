n1=input()
l1=[]
l2=[]
for i in range(0,len(n1)):
	if i%2!=0:
		l1.append(n[i])
	else:
		l2.append(n[i])
ls1=''.join(l1)
ls2=''.join(l2)
print(ls2,ls1)
 
