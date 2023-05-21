import math
def integer(x):
    if x>=0:
        sr=int(math.sqrt(x))
        return(sr*sr)==x
    return False
n=int(input())
if integer(n):
    print("True")
else:
    print("False")