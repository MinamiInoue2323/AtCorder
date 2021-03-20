h,w = map(int,input().split())
s = []
line_count = 0
for l in range(h):
    line = input()
    s.append([st for st in line])

#print(s)

#まずスタート地点の黒マスを探す
line_count = 0
for i in range(1,h):
    for j in range(1,w):
        count = 0
        if s[i-1][j-1] == '#':
            count += 1
        if s[i][j-1] == '#':
            count += 1
        if s[i-1][j] == '#':
            count += 1
        if s[i][j] == '#':
            count += 1
        
        if count == 1 or count == 3:
            line_count += 1
print(line_count)

    
            