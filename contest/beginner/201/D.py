h, w = map(int, input().split())
map_list = []
for i in range(h):
  a = list(input())
  new_list = []
  for j in a:
    if j == '+':
      new_list.append(1)
    else:
      new_list.append(-1)
  map_list.append(new_list)
#print(map_list)
dp = [[[0 for k in range(2)] for j in range(w)] for i in range(h)]
#print(dp)

for i in range(1,w):
  previous = dp[0][i-1]
  point = map_list[0][i]
  dp[0][i][0] = dp[0][i-1][0]
  dp[0][i][1] = dp[0][i-1][1]
  if sum(previous) % 2 == 0:
    dp[0][i][0] += point
  else:
    dp[0][i][1] += point

#print(dp)

for i in range(1,h):
  previous = dp[0][i-1]
  point = map_list[0][i]
  dp[i][0][0] = dp[i-1][0][0]
  dp[i][0][1] = dp[i-1][0][1]
  if sum(previous) % 2 == 0:
    dp[i][0][0] += point
  else:
    dp[i][0][1] += point

#print(dp)

for i in range(1,h):
  for j in range(1,w):
    pretop = dp[i - 1][j]
    preleft = dp[i][j - 1]
    point = map_list[i][j]
    if sum(pretop) % 2 == 0:
      if pretop[0] - pretop[1] < preleft[0] - preleft[1]:
        dp[i][j][0] = pretop[0] + point
        dp[i][j][1] = pretop[1]
      else:
        dp[i][j][0] = preleft[0] + point
        dp[i][j][1] = preleft[1]
    else:
      if pretop[0] - pretop[1] > preleft[0] - preleft[1]:
        dp[i][j][0] = pretop[0]
        dp[i][j][1] = pretop[1]+ point
      else:
        dp[i][j][0] = preleft[0]
        dp[i][j][1] = preleft[1] + point

#print(dp)

ans = dp[h-1][w-1]

if ans[0] > ans[1]:
  print("Takahashi")
elif ans[0] == ans[1]:
  print("Draw")
else:
  print("Aoki")