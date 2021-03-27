N,X = map(int,input().split())
X *=100
al = []
for i in range(N):
    V,P = map(int,input().split())
    al.append(V*P)

now = 0
for i in range(N):
    now+=al[i]
    if now > X:
        print(i+1)
        exit()
print(-1)