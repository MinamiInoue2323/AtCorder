def calc(s,n,m):
    ans = 0
    for c in s:
        ans = ans * n + int(c)
        if ans > m:
            return -1
    return ans

X = input()
M = int(input())

if len(X) == 1:
    if int(X) <= M:
        print(1)
    else:
        print(0)
    exit()


maxnum = max(map(int,X))
if calc(X,maxnum+1,M) < 0:
    print(0)
    exit()


mint = maxnum + 1
maxt = 10 ** 18 + 1

while mint+1 < maxt:
    mid = (maxt + mint) // 2
    if calc(X,mid,M) < 0:
        maxt = mid
    else:
        mint = mid

print(mint - maxnum)