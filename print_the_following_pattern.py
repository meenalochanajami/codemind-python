n=int(input())
c=65
for i in range(1,n+1):
    for j in range(1,n+1):
        ch=chr(c)
        print(ch,end=" ")
    print()
    c=c+1