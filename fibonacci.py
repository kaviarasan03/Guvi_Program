n=int(input())
c=0
k=1
for i in range(n):
  
  c=c+k
  c,k=k,c
  li.append(c)
print(*li)  
