N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

asum = 0
for i in range(N):
    asum += A[i] * B[i]

if asum == 0:
    print("Yes")
else:
    print("No")
