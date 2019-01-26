n=int(input())
li=list(map(int,input().split( )))
li1=[]
li2=[]
li3=[]
for i in range(0,n-1):
    
    for j in range(i+1,n):
        a=li[i]+li[j]
        li1.append(a)
        li2.append(li[i])
        li3.append(li[j])
c=0
for i in li1:

    if i==0:
        break
    c=c+1
    
d=li2[c]
e1=li3[c]
print(d,e1)
