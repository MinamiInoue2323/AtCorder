import sys
sys.setrecursionlimit(1000000)
a, b, c = map(int, input().split())



anslist = [[[-1 for k in range(101)] for j in range(101)] for i in range(101)]

def dp(anslist, i, j, k):
  if i == 100 or j == 100 or k == 100:
    anslist[i][j][k] = 0
    return 0

  if anslist[i][j][k] >= 0:
    return anslist[i][j][k]

  ans = 0
  ans += (i / (i + j + k)) * (1 + dp(anslist, i+1, j, k))
  ans += (j / (i + j + k)) * (1 + dp(anslist, i, j + 1, k))
  ans += (k / (i + j + k)) * (1 + dp(anslist, i, j, k + 1))
  anslist[i][j][k] = ans
  return ans


dp(anslist, a, b, c)

print(dp(anslist, a, b, c))