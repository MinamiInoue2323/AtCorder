
import math
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)

A,B,C,D = map(int,input().split())
gcd = my_lcm(C,D)
#print(gcd)

Bans = B // C + B // D - B // gcd
Aans = (A-1) // C + (A-1) // D - (A-1) // gcd
ans = B - A + 1 - (Bans - Aans)

print(ans)
