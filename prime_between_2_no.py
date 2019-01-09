

num1,num2=map(int,input().split( ))
li=[]
for num in range(num1,num2):
  if num > 1:

     for i in range(2,num):
         if (num % i) == 0:
             #print("no")

             break
     else:
         li.append(num)
for i in range(len(li)-1):
    print(li[i],end=" ")
print(li[len(li)-1])         
        


 
