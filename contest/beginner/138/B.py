N = int(input())
A = list(map(int,input().split()))

s = sum(A)
ans = 0

for i in A:
  ans += 1 / i

print("{:5f}".format(1 / ans))


