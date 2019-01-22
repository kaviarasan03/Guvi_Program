import math
c=0
l,r=map(int,input().split( ))
for j in range(l,r+1):
    s=math.sqrt(j)
    x=s - math.floor(s)
    if x==0:
        c=c+1
print(c)        
    
