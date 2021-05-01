n, d, h = map(int, input().split())
tower_list = []
for i in range(n):
  t = list(map(int, input().split()))
  tower_list.append(t)
seppen = 0
for t in tower_list:
  b = h - ((h - t[1]) / (d - t[0])) * d
  seppen = max(seppen, max(0, b))

print(seppen)
