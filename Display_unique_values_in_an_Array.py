n=int(input())
a=list(map(int,input().split()))
c=0
lst=[]
for i in a:
    k=a.count(i)
    if(k==1):
        lst.append(i)
if len(lst)==0:
    print(-1)
else:
    for i in lst:
        print(i,end=" ")