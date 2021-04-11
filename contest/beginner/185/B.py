N, M, T = map(int,input().split())
clist = []
for i in range(M):
  cafe = list(map(int,input().split()))
  clist.append(cafe)

now = N
ptime = 0

for c in clist:
  now = now - (c[0] - ptime)
  if now <= 0:
    print("No")
    exit()
  now = min(N, now + (c[1] - c[0]))
  ptime = c[1]

if now - (T - ptime) <= 0:
  print("No")
else:
  print("Yes")