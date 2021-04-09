N = int(input())
p = list(map(int,input().split()))

c = 0
n = 1
t = 0
for i in p:
  if i != n:
    c += 1
    if c == 1:
      t = i
    elif c == 2:
      if n != t:
        print("NO")
        exit()
    else:
      print("NO")
      exit()

  n += 1

print("YES")