N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
usel = A + B
l = N + M

usel.sort()
past = usel[0]
ans = []
i = 1
while i < N + M:
  now = usel[i]
  if past != now:
    ans.append(str(past))
    i += 1
    past = now
  else:
    if i == N + M - 1:
      break
    past=usel[i+1]
    i += 2

if usel[l - 2] != usel[l - 1]:
  ans.append(str(usel[l - 1]))

print(" ".join(ans))

