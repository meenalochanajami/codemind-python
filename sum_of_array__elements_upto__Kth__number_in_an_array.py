n=int(input())
l=list(map(int,input().split()))
k=int(input())
ind=l.index(k)
lis=[]
for i in range(ind+1):
    lis.append(l[i])
print(sum(lis))
    