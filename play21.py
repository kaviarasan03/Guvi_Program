a3,a2=map(int,input().split( ))
b1,b2=map(int,input().split( ))
c1,c2=map(int,input().split( ))
if a3==b1==c1 or a2==b2==c2:
    print("yes")
elif a3==a2 or b1==b2 or c1==c2:
    print("yes")
else:
    print("no")
