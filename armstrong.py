n1=int(input())
n=n1
sum1=0
while n>0:
    r=n%10
    n=n//10
    r=r*r*r
    sum1=sum1+r
if int(n1)==int(sum1):
    print("yes")
else:
    print("no")
