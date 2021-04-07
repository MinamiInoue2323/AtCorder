N = int(input())
Alist = []

m = 0
nm = 0
mc = 0
for i in range(N):
  a = int(input())
  if a > m :
    nm = m
    m = a
    mc = 1
  elif a > nm:
    nm = a
  elif a == m :
    mc += 1
  Alist.append(a)

for i in Alist:
  if i != m:
    print(m)
  else:
    if mc > 1:
      print(m)
    else:
      print(nm)



