n=int(input())
m=list(map(int,input().split()))
lis=[]
for i in m:
    if i not in lis:
        lis.append(i)
print(sum(lis))