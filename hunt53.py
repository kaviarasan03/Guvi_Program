n1,n2=input().split( )
s1=str(n1)
s2=int(n2)
li=[]
for i in range(0,len(s1)-s2+1):
    if len(li)!=0:
        li.append(" ")
    for j in range(i,i+s2):
        li.append(s1[j])
for j in li:
    print(j,end='')
        
    
