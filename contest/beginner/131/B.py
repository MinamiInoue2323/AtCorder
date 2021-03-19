N,L = map(int,input().split())
asum = (2 * L + N - 1) * N // 2

#L is first apple
if L <= 0 and 1 <= N + L:
  pass  
elif L <= 0:
    asum -= L + N - 1
else:
    asum -= L
print(asum)