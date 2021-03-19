coin10 = int(input())
coin2 = int(input())
coin1 = int(input())
x = int(input())/ 50
count = 0

for i in range(coin10+1):
    for j in range(coin2 + 1):
        for k in range(coin1 + 1):
            if i*10+j*2+k == x:
                count += 1

print(count)