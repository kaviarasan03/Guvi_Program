s=input()
l=list(s)
li=[]
li.append(l[0])
for i in range(0,len(l)):
	a=l[0]
	if a not in li:
		li.append(a)
	l.remove(a)
s1=""	
for i in li:
	s1=s1+i
r1=s1[::-1]
print(r1)
	
		
	
			
			
