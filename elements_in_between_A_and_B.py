n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
lis=[]
for i in l:
    if i>=a and i<=b:
        lis.append(i)
if len(lis)==0:
    print(-1)
else:
    for i in lis:
        print(i,end=" ")