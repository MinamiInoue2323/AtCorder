H,W,X,Y = map(int,input().split())
f = []
for i in range(H):
    f.append(list(input()))
smalli = X - 1
largei = X - 1
smallj = Y - 1
largej = Y - 1

while smalli >= 0:
    if f[smalli][Y-1] == "#":
        break
    smalli -= 1

while largei < H:
    if f[largei][Y-1] == "#":
        break
    largei += 1

while smallj >= 0:
    if f[X-1][smallj] == "#":
        break
    smallj -= 1


while largej < W:
    if f[X-1][largej] == "#":
        break
    largej += 1

print((largei - smalli - 1)+(largej - smallj - 1) - 1)