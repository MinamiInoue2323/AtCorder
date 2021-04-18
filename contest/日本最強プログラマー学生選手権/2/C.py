import math
a, b = map(int,input().split())

d = b - a
i = d

while i != 1:
  if math.floor(b / i) - math.ceil(a / i) >= 1:
    print(i)
    exit()
  i -= 1
print(1)
