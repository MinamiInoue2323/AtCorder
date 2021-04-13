N = int(input())
H = list(map(int,input().split()))
H.reverse()

past = 10 ** 9 + 1
for masu in H:
  if masu > past:
    if masu - past >= 2:
      print("No")
      exit()
    else:
      past = masu - 1
  else:
    past = masu

print("Yes")