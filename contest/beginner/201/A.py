a, b, c = map(int, input().split())

setlist = [[a,b,c],[a,c,b],[b,a,c],[b,c,a],[c,a,b],[c,b,a]]

for i in setlist:
  if i[2] - i[1] == i[1] - i[0]:
    print("Yes")
    exit()
print("No")