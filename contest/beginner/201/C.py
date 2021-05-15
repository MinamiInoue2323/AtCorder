memory = list(input())
n_maru = 0
n_hatena = 0
n_batsu = 0

for i in memory:
  if i == 'o':
    n_maru += 1
  elif i == 'x':
    n_batsu += 1
  else:
    n_hatena += 1

if n_maru > 4 or n_maru + n_hatena == 0:
  print(0)
  exit()

count = 0

#maruがない場合
if n_maru == 0:
  print(n_hatena ** 4)
  exit()

#all maru
if n_maru == 1:
  count += 1
  if n_hatena > 0:
    count += 4 * n_hatena ** 3
    count += 6 * n_hatena ** 2
    count += 4 * n_hatena ** 1
elif n_maru == 2:
  count += 14
  if n_hatena > 0:
    count += 12 * n_hatena ** 2
    count += 24 * n_hatena ** 1
elif n_maru == 3:
  count += 36
  if n_hatena > 0:
    count += 24 * n_hatena ** 1
elif n_maru == 4:
  print(24)
  exit()

print(count)