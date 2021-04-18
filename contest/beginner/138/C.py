N = int(input())
v = list(map(int,input().split()))
v.sort(reverse=True)
ans = v.pop()

for i in range(N-1):
  ans = (ans + v.pop()) / 2

print(ans)
