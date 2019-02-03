n1=input()
n2=input()
if n2 in n1:
    for j in range(0,len(n1)):
        if n2[0]==n1[j]:
            print(j)
            break
else:
    print("-1")
