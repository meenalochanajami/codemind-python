n=int(input())
c=0
l=list(map(str,input().split()))
for i in l:
    if len(i)%2==0:
        c+=1
print(c)