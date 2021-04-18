r1, c1 = map(int,input().split())
r2, c2 = map(int, input().split())

if r1 == r2 and c1 == c2:
  print(0)
  exit()

x = r2 - r1
y = c2 - c1

if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
  print(1)
  exit()

if  (r1 + c1 - r2 + c2) % 2 == 0 or abs(r1 - r2) + abs(c1 - c2) <= 6:
  print(2)
  exit()

r3 = r2
c3 = c1
if c2 > c1:
  c3 += abs(r2 - r1)
else:
  c3 -= abs(r2 - r1)

if abs(r3 - r2) + abs(c3 - c2) <= 3:
  print(2)
  exit()

print(3)