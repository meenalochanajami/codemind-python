t=int(input())

for i in range(t):
    n=input()
    c=0
    for j in n:
        if j>='0' and j<='9':
            c+=1
    if(c!=0):
        print("Yes")
    else:
        print("No")