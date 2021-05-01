s = input()
count = 0
for i in range(9):
  if s[i:i+4] == "ZONe":
    count += 1

print(count)