K, X = map(int,input().split())

left = max(-1000000, X - K + 1)
right = min(1000000, X + K - 1)

ans=[]
for i in range(left,right+1):
  ans.append(str(i))

print(" ".join(ans))