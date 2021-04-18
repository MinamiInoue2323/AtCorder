n, x = map(int,input().split())
s = input()

ans = x
for i in s:
  if i == "o":
    ans += 1
  else:
    ans = max(0,ans - 1)

print(ans)