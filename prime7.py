num=int(input())
if num>1:
    for j in range(2,num):
        if num%j==0:
            
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
    
        
