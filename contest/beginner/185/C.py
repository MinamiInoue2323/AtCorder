L = int(input())

if L == 12:
  print(1)
  exit()

a = L - 1
b = a - 11
c = 1

ans = 1

for i in range(b):
  ans *= a
  a -= 1

for i in range(b):
  ans //= c
  c += 1

print(ans)