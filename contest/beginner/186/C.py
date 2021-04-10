def Base_10_to_n(X, n):
  if (int(X/n)):
      return Base_10_to_n(int(X/n), n)+str(X%n)
  return str(X%n)

N = int(input())
s = 0

for i in range(1,N+1):
  eight = Base_10_to_n(i,8)
  ten = str(i)
  if "7" not in eight and "7" not in ten:
    s += 1

print(s)