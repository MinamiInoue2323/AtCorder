N,C = map(int,input().split())
event = []

for i in range(N):
    a,b,c = map(int,input().split())
    event.append((a - 1, c))
    event.append((b, -c))

event.sort()

ans = 0
fee = 0
t = 0

for time, price in event:
    if t != time:
        ans += min(C,fee) * (time - t)
        t = time
    fee += price

print(ans)

