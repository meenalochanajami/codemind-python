n=int(input())
l=list(map(int,input().split()))
li=[]
a,b=map(int,input().split())
for i in l:
    if i>=a and i<=b:
        pass
    else:
        li.append(i)

print(sum(li))