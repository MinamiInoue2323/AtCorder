import math
x, y, z = map(int,input().split())

print(max(0, math.ceil(y / x * z - 1)))