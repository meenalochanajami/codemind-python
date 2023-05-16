n=int(input())
s=list(map(int,input().split()))
s1=0
s2=0
for i in range(len(s)):
    if i%2==0:
        s1=s1+s[i]
    else:
        s2=s2+s[i]
if (s2-s1)==0:
    print("YES")
else:
    print("NO")