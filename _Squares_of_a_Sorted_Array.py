n=int(input())
l1=[]
l=list(map(int,input().split()))
for i in range(len(l)):
    l1.append((l[i]*l[i]))
l1.sort()
for i in l1:
    print(i,end=" ")