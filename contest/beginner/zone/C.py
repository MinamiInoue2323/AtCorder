def calscore(member_list):
  s = [0,0,0,0,0]
  s[0] = max(member_list[0][0],member_list[1][0],member_list[2][0])
  s[1] = max(member_list[0][1],member_list[1][1],member_list[2][1])
  s[2] = max(member_list[0][2],member_list[1][2],member_list[2][2])
  s[3] = max(member_list[0][3],member_list[1][3],member_list[2][3])
  s[4] = max(member_list[0][4],member_list[1][4],member_list[2][4])
  all_s = min(s)
  minin =[i for i, v in enumerate(s) if v == all_s]
  return [all_s, minin]


def findreplace(oldlist, newmember):
  kouho = []
  kouho.append([0, calscore([oldlist[0], oldlist[1],newmember])])
  kouho.append([1, calscore([oldlist[1], oldlist[2],newmember])])
  kouho.append([2, calscore([oldlist[2], oldlist[0],newmember])])
  kouho.append([3, calscore([oldlist[0], oldlist[1],oldlist[2]])])
  k = [0,0,0]
  index = 0
  for i in kouho:
    if k[0] < i[1][0]:
      k[0] = i[1][0]
      k[1] = i[1][1]
      k[2] = i[0]
  return k




n = int(input())
team_list = []
for i in range(n):
  a = list(map(int, input().split()))
  team_list.append(a)

#first
members = team_list[:3].copy()
score = [0,0,0,0,0]
score[0] = max(members[0][0],members[1][0],members[2][0])
score[1] = max(members[0][1],members[1][1],members[2][1])
score[2] = max(members[0][2],members[1][2],members[2][2])
score[3] = max(members[0][3],members[1][3],members[2][3])
score[4] = max(members[0][4],members[1][4],members[2][4])
allscore = min(score)
minindex = [i for i, v in enumerate(score) if v == allscore]

for i in range (n - 3):
  m = team_list[i + 3]
  r_flag = False
  for j in minindex:
    if m[j] > j:
      r_flag = True
  if r_flag:
    r = findreplace(members, m)
    if r[2] == 0:
      members[2] = m
      allscore = r[0]
      minindex = r[1]
    elif r[2] == 1:
      members[0] = m
      allscore = r[0]
      minindex = r[1]
    elif r[2] == 2:
      members[1] = m
      allscore = r[0]
      minindex = r[1]

print(allscore)


