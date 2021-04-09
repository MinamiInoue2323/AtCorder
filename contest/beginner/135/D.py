S = input()
sl = len(S)
dp = [[0 for i in range(13)] for j in range(sl+1)]
mod = 10 ** 9 + 7

dp[0][0] = 1

for i in range(sl):
  c = S[i]
  if c == "?":
    c = -1
  else:
    c = int(c)
  
  for j in range(10):
    if c != -1 and c != j:
      continue

    for k in range(13):
      dp[i+1][(k * 10 + j) % 13] += dp[i][k]
  
  for j in range(13):
    dp[i+1][j] %= mod
print(dp[sl][5])

  

