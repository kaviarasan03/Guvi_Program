s=input()
s1=s[::-1]
li=[]
li1=["a","e","i","o","u"]
for i in s1:
    if i not in li1:
        li.append(i)
num(*li)        
        
