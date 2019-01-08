n=int(input())
sum1=0
while n>0:
    r=n%10
    n=int(n/10)
    r=r*r*r
    sum1=sum1+r
print(sum1)    
if n==sum1:
    print("yes")
else:
    print("no")
