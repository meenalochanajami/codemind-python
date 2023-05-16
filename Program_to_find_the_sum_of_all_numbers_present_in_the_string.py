s=input()
lst=[]
for i in s:
    if i>='0' and i<='9':
        lst.append(i)
n1=list(map(int,lst))
print(sum(n1))