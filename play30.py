s1,s2,n1=input().split( )
s1=str(s1)
s2=str(s2)
n1=int(n1)
c=0
for i in range(0,len(s1)):
    if s1[i]!=s2[i]:
        c+=1
if c==n1:
    print("yes")
else:
    print("no")
    
