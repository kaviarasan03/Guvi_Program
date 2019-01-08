

num1,num2=map(int,input().split( ))
for num in range(num1,num2):
  if num > 1:

     for i in range(2,num):
         if (num % i) == 0:
             #print("no")

             break
     else:
         print(num,end=" ")


 
