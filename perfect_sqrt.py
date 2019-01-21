import math 
  
def isPerfectSquare(x): 
  
     
    sr = math.sqrt(x) 
   
   
    return ((sr - math.floor(sr)) == 0) 
  
 
  
x1,x3 = map(int,input().split( ))
x=x1*x3
if (isPerfectSquare(x)): 
    print("yes") 
else: 
    print("no") 
  
