a3,a2=map(int,input().split( ))
for i in range(a3,0,-1):
    if a3%i==0 and a2%i==0:
        print(i)
        break
