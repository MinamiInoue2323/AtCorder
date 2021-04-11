import math
R, X, Y = map(int,input().split())

sd = math.sqrt(X ** 2 + Y ** 2)

if sd < R:
  print(2)
  exit()

print(math.ceil(sd / R))