N = int(input())
tlist=[]
aoki = 0

for i in range(N):
  a,b = map(int,input().split())
  aoki += a
  tlist.append(a * 2 + b)

tlist.sort(reverse=True)
#print(tlist)
s = 0
c = 0
for i in tlist:
  c += 1
  s += i
  if s > aoki:
    print(c)
    exit()