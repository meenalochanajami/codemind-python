n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
lis=[]
lis2=[]
for i in l:
    if i>=a and i<=b:
        lis.append(i)
for i in l:
    if i not in lis:
         lis2.append(i)
if len(lis2)==0:
    print(-1)
else:
    print(min(lis2))