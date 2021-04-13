S = input()
N = len(S)

past = "R"
p = 0
borders = []
for i in S:
  if past != i:
    borders.append(p - 1)
    past = i
  p += 1
borders.append(N - 1 )

ans = [0] * N
#true means "R" false means "L"
nowl = True
past = -1
for i in borders:
  n = i - past
  if nowl:
    ans[i] += (n + 1) // 2
    ans[i + 1] += n // 2
    nowl = False
  else:
    #print("left")
    ans[past] += n // 2
    ans[past + 1] += (n + 1) // 2
    nowl = True
  past = i
  #print(n)
  #print(ans)

print(*ans)

