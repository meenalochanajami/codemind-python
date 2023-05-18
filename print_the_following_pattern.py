n=int(input())
a=1
for i in range(n+1,1,-1):
    for j in range(1,i):
        print(j,end="")
        i=i-1
    print("")   