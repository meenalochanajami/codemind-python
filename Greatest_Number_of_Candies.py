n=int(input())
l=list(map(int,input().split()))
a=int(input())
k=max(l)
for i in l:
    m=i+a
    if m>=k:
        print("True",end=" ")
    else:
        print("False",end=" ")
