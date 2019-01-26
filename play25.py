n1=int(input())
li=list(map(str,input().split( )))

li.sort()
li=sorted(li,key=len)
print(*li)
