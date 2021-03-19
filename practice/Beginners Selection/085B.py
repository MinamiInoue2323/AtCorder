N = int(input())

a = [int(input()) for i in range(N)]
a.sort()

now = 0

count = 0
for i in a:
    if i != now:
        now = i
        count += 1

print(count)
