n = int(input())
a = list(map(int, input().split()))

cnt_list = [0] * 200

for i in a:
  cnt_list[i % 200] += 1

ans  = 0

for i in cnt_list:
  if i < 2:
    continue
  else:
    ans += i * (i - 1) // 2

print(ans)