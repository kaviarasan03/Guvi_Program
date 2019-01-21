num=int(input())


li=[]


   
for j in range(1,num+1):
    if (num % j) == 0:
        li.append(j)
print(*li)        
       
       

       

