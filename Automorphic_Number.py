n=int(input())
d=len(str(n))
s=n*n
l=s%pow(10,d)
if l==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")