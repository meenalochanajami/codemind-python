n=int(input())
x=list(map(int,input().split()))
lst=[]
for i in x:
    k=x.count(i)
    if k==1:
        lst.append(i)
if len(lst)==0:
    print(-1)
else:
    print(max(lst))

        