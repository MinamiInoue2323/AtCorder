N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

s = 0
p = A[0]
for i in range(N):
  yu = B[i]
  
  beat = min(yu,p)
  s += beat
  yu -= beat

  p = A[i+1]
  beat = min(yu,p)
  s += beat
  p -= beat

print(s)


