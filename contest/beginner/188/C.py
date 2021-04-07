N = int(input())
A = list(map(int,input().split()))

half = 2 ** N // 2
left = A[:half]
right = A[half:]
#print(left)
#print(right)
lmax = max(left)
rmax = max(right)

if lmax > rmax:
    print(A.index(rmax) + 1)
else:
    print(A.index(lmax) + 1)