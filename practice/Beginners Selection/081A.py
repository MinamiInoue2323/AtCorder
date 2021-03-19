s=int(input())
sum = 0

for i in range(3):
    if s % 10 == 1:
        sum+=1
    s //= 10
print(sum)
