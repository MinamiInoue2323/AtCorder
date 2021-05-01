N = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

amax = max(a)
bmin = min(b)

if amax > bmin:
  print(0)
  exit()

print(bmin - amax + 1)