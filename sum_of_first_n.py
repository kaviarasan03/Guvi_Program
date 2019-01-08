n,k=map(int,input().split( ))
li=[]
for i in range(n):
    a=int(input())
    li.append(a)
sum1=0

for i in range(k):
    sum1=sum1+li[i]
print(sum1)

