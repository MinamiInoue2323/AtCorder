import copy
n = int(input())
a = list(map(int, input().split()))
cnt_list = [[0 for i in range(200)] for j in range(n+1)]
include_list=[[] for i in range(200)]
a.sort()
#print(include_list)
for i in range(n):
  now = a[i]
  for j in range(200):
    if cnt_list[i][j] > 0:
      if cnt_list[i][(j + now) % 200] > 0:
        #print(include_list)
        print("Yes")
        ans1 = include_list[j]
        ans1.append(i+1)
        ans1_show = [str(b) for b in ans1]
        print(len(ans1)," ".join(ans1_show))
        ans2 = include_list[(j + now) % 200]
        ans2_show = [str(b) for b in ans2]
        print(len(ans2)," ".join(ans2_show))
        exit()
      else:
        #print(include_list)
        #print(j)
        cnt_list[i+1][(j + now) % 200] += cnt_list[i][j]
        include_list[(j + now) % 200] = copy.copy(include_list[j])
        include_list[(j + now) % 200].append(i+1)
      cnt_list[i+1][j] += cnt_list[i][j]
  if cnt_list[i+1][now % 200] > 0:
    #print(include_list)
    print("Yes")
    ans1 = include_list[now % 200]
    ans1_show = [str(b) for b in ans1]
    print(len(ans1)," ".join(ans1_show))
    print(1,i+1)
    exit()
  else:
    cnt_list[i+1][now % 200] += 1
    include_list[now % 200].append(i+1)
#print(cnt_list)
# for i in cnt_list[n]:
#   if i > 1:
#     print("Yes")
#     exit()
print("No")

