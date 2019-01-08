n1=int(input())
li=[]
for i in range(n1):
    ar=int(input())
    li.append(ar)
srt=sorted(li)
m=int(len(li)/2)
print(srt[m])
