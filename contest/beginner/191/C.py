h,w = map(int,input().split())
s = []
line_count = 0
for l in range(h):
    line = input()
    s.append([st for st in line])

print(s)

#まずスタート地点の黒マスを探す
start_masu = [0,0]
for i in range(1,h):
    for j in range(1,w):
        if s[i][j] == '#':
            start_masu[0] = i
            start_masu[1] = j
            break
    if start_masu[0] != 0 and start_masu[1] != 0:
        break
    

print(start_masu)
now_masu = start_masu
now_hen = ""
past_hen = ""
if s[now_masu[0],now_masu[1]+1] = "#":
    now_masu[1] +=1
else:
    now_hen = "right"
line_count += 1


while now_masu == start_masu and now_hen == "top":
    if now_hen =="top":
        if s[now_masu[0],now_masu[1]+1] = "#":
            now_masu[1]+=1
        else:
            
    
