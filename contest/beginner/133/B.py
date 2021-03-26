import math

N,D = map(int,input().split())
plist = []
for i in range(N):
    p = list(map(int,input().split()))
    plist.append(p)
count = 0
i = 0
while i < N:
    j = N-1
    while  i < j:
        asum = 0
        for k in range(D):
            asum += (plist[i][k]-plist[j][k]) ** 2
        if math.sqrt(asum) % 1 == 0:
            count += 1
        j -=1
    i+=1

print(count)

