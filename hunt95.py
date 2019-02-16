n1=int(input())
li=[]

if n1<=2:
    print("0")
else:
    
    for i in range(2,n1):
        num=i
        for j in range(2,num):
            if (num % j) == 0:
                break
        else:
            li.append(num)
    print(*li)       
       
        
