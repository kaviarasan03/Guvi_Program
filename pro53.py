n1=input()
l=list(n1)
li=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','m','n','b','v','c','x','z']
for i in li:
    if i not in l:
        print("no")
        break
else:
    print("yes")
        
