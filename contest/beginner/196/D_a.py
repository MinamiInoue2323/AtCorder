h,w,a,b = map(int,input().split())
ans = 0
 
def dfs(i,bit,A,B):
    if i == h * w:
        global ans
        ans += 1
        return
    
    if bit >> i & 1:
        dfs(i+1,bit,A,B)
        return
    
    if B:
        dfs(i+1,bit | 1 << i, A, B-1)
    if A:
        if i % w !=w - 1 and not bit & 1 << (i + 1):
            dfs(i+1,bit | 1 << i |1 << (i + 1), A - 1, B)
        if i + w < h * w:
            dfs(i+1,bit | 1 << i |1 << (i + w), A - 1, B)





dfs(0,0,a,b)
print(ans)
