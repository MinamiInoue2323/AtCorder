N = int(input())
A = list(map(int, input().split()))
minc = 99999

for a in A:
    count = 0
    while a % 2 == 0:
        count+=1
        a //= 2
    if count < minc:
        minc = count
print(minc)
