n=int(input())
l=list(map(int,input().split()))
lis=[]
k=0
for i in l:
    if i not in lis:
        lis.append(i)
for i in lis:
    if i%2!=0:
        k=k+i
print(k)
    