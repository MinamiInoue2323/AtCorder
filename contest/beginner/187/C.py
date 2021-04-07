N = int(input())
wlist =[]

for i in range(N):
  w = input()
  wlist.append(w[::-1])

wlist.sort()


past = ""
zero=False

for w in wlist:
  if w[-1] == "!":
    if w[:-1] == past:
      print(past[::-1])
      exit()
  past = w

print("satisfiable")