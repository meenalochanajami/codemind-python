n=int(input())
l=list(map(int,input().split()))
lis=[]
for i in l:
    if i not in lis:
        lis.append(i)
for i in lis:
    print(i,end=" ")
    