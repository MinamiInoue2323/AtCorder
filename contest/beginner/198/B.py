N = input()
rn = N[::-1]
rn = str(int(rn))


if rn == 0:
  print("Yes")
  exit()

r = len(rn) - 1
l = 0
while l < r:
  if rn[l] != rn[r]:
    print("No")
    exit()
  l += 1
  r -= 1
print("Yes")