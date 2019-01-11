n=int(input())
st=input()
s1=st[::-1]
li=[]
li1=["a","e","i","o","u"]
for i in s1:
    if i not in li1:
        li.append(i)
 
for i in range(len(li)-1):
	print(li[i],end="")
print(li[len(li)-1])	
