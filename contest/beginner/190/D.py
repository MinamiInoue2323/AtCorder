N = int(input())
count = 0

for i in range(1,int(N/1.5)+1):
    div = N / i
    if i % 2 == 0:
        if div % 1 == 0.5:
            #print(i)
            count += 1
    else:
        if div % 1 == 0:
            #print(i)
            count += 1

if N % 2 == 0:
    print(count+1)
else:
    print(count+2)
