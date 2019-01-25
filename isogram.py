n1=input()
s=list(n1)
for i in range(0,len(s)):
    a=s[0]
    s.remove(s[0])
    if a in s:
        print("No")
        break
    s.append(a)
else:
    print("Yes")
    
