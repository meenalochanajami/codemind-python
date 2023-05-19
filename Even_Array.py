n=int(input())
l=list(map(int,input().split()))
c=0
c1=len(l)
c2=0
for i in range(n):
    if l[i]%2==0:
        c=c+1

if c==c1:
    print("True")
else:
    print("False")
            