N = int(input())
A = list(map(int,input().split()))

ans = 0

for i in range(N):
    mini = A[i]
    j = i
    while j < N:
        mini = min(mini,A[j])
        ans = max(ans,(j - i + 1) * mini)    
        j += 1
print(ans)







