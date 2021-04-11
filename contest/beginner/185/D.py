import math
N, M = map(int,input().split())
if M == 0:
  print(1)
  exit()

A = list(map(int, input().split()))
if M == N:
  print(0)
  exit()
A.sort()

past = 0
mini = 10 ** 9 + 1
wlist = []
for blue in A:
  d = blue - past - 1
  if d == 0:
    past = blue
    continue
  mini = min(mini, d)
  wlist.append(d)
  past = blue
d = N + 1 - past - 1
wlist.append(d)

#print(mini)
#print(wlist)
ans = 0
for i in wlist :
  #print(math.ceil(i / mini))
  ans += math.ceil(i / mini)

print(ans)

