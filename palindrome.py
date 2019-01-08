num=int(input())
s=str(num)
n=(int(s[::-1]))
if n<=1000:
	if n==num:
		print("yes")
	else:
		print("no")
  
