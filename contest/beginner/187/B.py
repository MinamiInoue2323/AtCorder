N = int(input())

xylist = []

for i in range(N):
  x,y = map(int,input().split())
  xylist.append([x, y])

count = 0
i = 0
while i < N:
  j = i+1
  p = xylist[i]
  while j < N:
    q =xylist[j]
    k = (q[1] - p[1]) / (q[0] - p[0])
    if k >= -1 and k <= 1:
      count += 1
    j += 1
  i += 1
print(count)
