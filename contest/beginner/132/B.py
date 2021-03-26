n = int(input())
p = list(map(int,input().split()))
count = 0

for i in range(1,n-1):
    plist = [p[i-1],p[i],p[i+1]]
    if sorted(plist)[1] == p[i]:
        count += 1
print(count)