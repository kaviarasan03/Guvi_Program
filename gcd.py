n1,n2=map(int,input().split( ))

for i in range(2,n1+1):
    if n1%i==0 and n2%i==0:
        print(i)
        break
else:
    print("1")
    
