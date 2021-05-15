import copy
n = int(input())
a = list(map(int, input().split()))
include_list=[[] for i in range(200)]
alen = min(len(a), 8)

for i in range(1, 2 ** alen):
  s = []
  mod = 0
  for j in range(alen):
    if i & (1 << j):
      s.append(j+1)
      mod += a[j]
      mod %= 200
  if len(include_list[mod]) > 0:
    print("Yes")
    print(len(include_list[mod]),*include_list[mod])
    print(len(s),*s)
    exit()
  else:
    include_list[mod] = s
print("No")

