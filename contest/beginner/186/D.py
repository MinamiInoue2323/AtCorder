N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)

s = 0
nowm = N - 1

for i in A:
  s += nowm * i
  nowm -= 2

print(s)
