L,R = map(int,input().split())

if L % 2019 == 0 or L // 2019 != R // 2019:
    print(0)
else:
    ans = 2020
    i = L
    while i < R:
        j = R
        while i < j:
            ans = min(ans,(i*j) % 2019)
            j -= 1
        i += 1
    print(ans)
