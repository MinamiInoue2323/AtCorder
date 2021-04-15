import heapq

N, M = map(int,input().split())
tasks=[]
for i in range(N):
  t = list(map(int,input().split()))
  tasks.append(t)

tasks.sort()

tq = []
ans = 0
nowi = 0
heapq.heapify(tq)
for i in range(1, M+1):
  if nowi != N:
    while tasks[nowi][0] <= i:
      heapq.heappush(tq,tasks[nowi][1] * (-1))
      nowi += 1
      if nowi == N:
        break
  if len(tq) != 0:
    ans += heapq.heappop(tq) * -1

print(ans)




