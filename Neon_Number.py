k=int(input())
n=k*k
s=0
while(n):
    r=n%10
    s=s+r
    
    n=n//10
if k==s:
    print("Neon Number")
else:
    print("Not Neon Number")