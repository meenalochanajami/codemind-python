p,r,t=map(float,input().split())
Amount = p * (pow((1 + r / 100), t))
print("%.2f"%Amount)