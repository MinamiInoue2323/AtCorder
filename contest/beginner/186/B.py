H,W = map(int,input().split())
hwlist=[]
m = 1000
s = 0
for i in range(H):
  a = list(map(int,input().split()))
  for j in a:
    m = min(m,j)
    s += j

print(s - (m * H * W))
