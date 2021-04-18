mod = 10 ** 9 + 7
def pow1(x, n):
    if n == 0: return 1
    value = pow1(x, int(n / 2))
    value *= value
    if n % 2 == 1: value *= x
    return value % mod

n, p = map(int,input().split())

ans = p - 1


if p == 2:
  if n == 1:
    print(p-1)
  else:
    print(0)
  exit()

m = p - 2

m2 = pow1(m,n-1)

ans *= m2

print(ans % mod)