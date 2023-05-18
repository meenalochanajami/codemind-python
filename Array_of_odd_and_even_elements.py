n=int(input())
l=list(map(int,input().split()))
li=[]
for i in l:
    if i%2!=0:
        li.append(i)
for i in l:
    if i%2==0:
        li.append(i)
for i in li:
    print(i,end=" ")
    
    
        