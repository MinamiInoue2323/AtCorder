n, p = map(int,input().split())

ans = p - 1
mod = 10 ** 9 + 7

if p == 2:
  if n == 1:
    print(p-1)
  else:
    print(0)
  exit()

m = p - 2

n -= 1
if n % 2 == 0:
  m *= m
  for i in range(n // 2):
    ans = (ans * m) % mod
else:
  ans *= m
  m *= m
  for i in range((n-1)//2):
    ans = (ans * m) % mod

print(ans)
