n=int(input())
l=list(map(int,input().split()))
s=0
s1=0
for i in range(n//2 +1):
    s=s+i

for j in range((n//2)+1,n+1,1):
    s1=s1+j

print(abs(s-s1))