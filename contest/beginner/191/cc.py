h,w = map(int,input().split())
s = []
line_count = 0
for l in range(h):
    line = input()
    s.append([st for st in line])

#print(s)

kyokai = []

for i in range(h+1):
    zeros = []
    for j in range(w+1):
        zeros.append(False)
    kyokai.append(zeros)

#print(kyokai)

for i in range(1,h):
    for j in range(1,w):
        if s[i][j] == '#':
            if s[i+1][j] == '.':
                kyokai[i+1][j] = True
                kyokai[i+1][j+1] = True
            if s[i-1][j] == '.':
                kyokai[i][j] = True
                kyokai[i][j+1] = True
            if s[i][j-1] == '.':
                kyokai[i][j] = True
                kyokai[i+1][j] = True
            if s[i][j+1] == '.':
                kyokai[i][j+1] = True
                kyokai[i+1][j+1] = True

for i in kyokai:
    print(i)

#まずスタート地点の黒マスを探す
start_masu = [0,0]
end_flag = False
for i in range(h+1):
    for j in range(w+1):
        if kyokai[i][j]:
            start_masu[0] = i
            start_masu[1] = j
            end_flag = True
            break
    if end_flag:
        break
now_masu = [0,0]
now_masu[0] = start_masu[0]
now_masu[1] = start_masu[1]
direction = ""
line_count = 1
if kyokai[start_masu[0]+1][start_masu[1]]:
    now_masu[0]+=1
    direction = "down"
elif kyokai[start_masu[0]-1][start_masu[1]]:
    now_masu[0]-=1
    direction = "top"
elif kyokai[start_masu[0]][start_masu[1]-1]:
    now_masu[1]-=1
    direction = "left"
elif kyokai[start_masu[0]][start_masu[1]+1]:
    now_masu[1]+=1
    direction = "right"
#print(now_masu)
#print(start_masu)

while now_masu != start_masu:
    print(now_masu)
    print(direction)
    if direction == "down":
        if kyokai[now_masu[0]+1][now_masu[1]]:
            now_masu[0]+=1
            continue
        else:
            if kyokai[now_masu[0]][now_masu[1]-1]:
                now_masu[1]-=1
                direction = "left"
            elif kyokai[now_masu[0]][now_masu[1]+1]:
                now_masu[1]+=1
                direction = "right"
            elif kyokai[now_masu[0]+1][now_masu[1]]:
                now_masu[0]+=1
                direction = "down"
            line_count+=1
            
    elif direction == "top":
        if kyokai[now_masu[0]-1][now_masu[1]]:
            now_masu[0]-=1
            continue
        else:
            if kyokai[now_masu[0]-1][now_masu[1]]:
                now_masu[0]-=1
                direction = "top"
            elif kyokai[now_masu[0]][now_masu[1]-1]:
                now_masu[1]-=1
                direction = "left"
            elif kyokai[now_masu[0]][now_masu[1]+1]:
                now_masu[1]+=1
                direction = "right"
            line_count+=1
    elif direction == "left":
        if kyokai[now_masu[0]][now_masu[1]-1]:
            now_masu[1]-=1
            continue
        else:
            if kyokai[now_masu[0]-1][now_masu[1]]:
                now_masu[0]-=1
                direction = "top"
            elif kyokai[now_masu[0]][now_masu[1]-1]:
                now_masu[1]-=1
                direction = "left"
            elif kyokai[now_masu[0]+1][now_masu[1]]:
                now_masu[0]+=1
                direction = "down"
            line_count+=1
    elif direction == "right":
        if kyokai[now_masu[0]][now_masu[1]+1]:
            now_masu[1]+=1
            continue
        else:
            if kyokai[now_masu[0]-1][now_masu[1]]:
                now_masu[0]-=1
                direction = "top"
            elif kyokai[now_masu[0]][now_masu[1]+1]:
                now_masu[1]+=1
                direction = "right"
            elif kyokai[now_masu[0]+1][now_masu[1]]:
                now_masu[0]+=1
                direction = "down"
            line_count+=1


print(line_count)
    

