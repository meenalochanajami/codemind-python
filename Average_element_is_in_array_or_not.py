n=int(input())
c=0
l=list(map(int,input().split()))
k=sum(l)
a=k//n
for i in l:
    if i==a:
        c=1
if c==1:
    print("True")
else:
    print("False")
    