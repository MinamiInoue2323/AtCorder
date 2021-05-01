from collections import deque

s = input()
ansl = deque()
c= 0
for i in s:
  if i == 'R':
    c += 1
    continue
  if len(ansl) == 0:
    ansl.append(i)
    continue
  if c % 2 == 0:
    a = ansl.pop()
    if a != i:
      ansl.append(a)
      ansl.append(i)
  else:
    a = ansl.popleft()
    if a != i:
      ansl.appendleft(a)
      ansl.appendleft(i)

if c % 2 == 0:
  print("".join(ansl))
else:
  print("".join(ansl)[::-1])