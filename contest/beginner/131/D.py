N = int(input())
ab = [list(map(int,input().split())) for _ in range(N)]
ab.sort(key=lambda x: x[1])
#print(ab)

time = 0
for i in ab:
    time += i[0]
    if time > i[1]:
        print("No")
        exit()
print("Yes")
