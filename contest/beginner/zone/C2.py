n = int(input())
member_list = []
for i in range(n):
  a = tuple(map(int, input().split()))
  member_list.append(a)

def check(x):
  s = set()
  for m in member_list:
    s.add(sum(1 << i for i in range(5) if m[i] >= x))
  for x in s:
    for y in s:
      for z in s:
        if x | y | z == 31:
          return True
  return False

ok = 0
ng = 10 ** 9 + 1

while ng - ok > 1:
  cen = (ok + ng) // 2
  if check(cen):
    ok = cen
  else:
    ng = cen
print(ok)