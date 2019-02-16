n1=input().split( )
li=[]
for i in range(0,len(n1)):
   if i%2!=0: 
      li.append(n1[i])
   else:
      a=n1[i]
      b=a[::-1]
      li.append(b)
      a=''
      b=''
print(*li)
