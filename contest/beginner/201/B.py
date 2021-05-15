n = int(input())
mtlist=[]
for i in range(n):
  name, tall = map(str, input().split())
  mtlist.append([int(tall), name])

mtlist.sort(reverse=True)

print(mtlist[1][1])