import collections

N = int(input())
slist = []
for i in range(N):
  s = sorted(input())
  slist.append("".join(s))

c = collections.Counter(slist)

ans = 0
for i in c.values():
  ans += i * (i-1) // 2

print(ans)
