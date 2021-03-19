a = list(map(int,input().split()))
N = a[0]
A = a[1]
B = a[2]

def total(n):
    if n < 1:
        return 0
    return (n % 10) + total(n // 10)

count = 0
for i in range(1,N+1):
    sum = total(i)
    if sum >= A and sum <= B:
        count += i

print(count)

    