import itertools
N = int(input())
A = list(map(int,input().split()))
ans = 1 << 30

if N == 1:
    print(A[0])
    exit()

for i in range(1,N):
    for j in list(itertools.combinations(range(N-1), i)):
        a = 0
        now = 0
        b = 0
        while now < N:
            b = b | A[now]
            if now in j:
                a = a ^ b
                b = 0
            now += 1
        a = a ^ b
        
        ans = min(a,ans)
print(ans)

        
        
