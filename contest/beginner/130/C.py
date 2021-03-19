W,H,x,y = map(int,input().split())

area = W * H / 2
is_hukusu = 0

if W / 2 == x and H / 2 == y:
    is_hukusu = 1

print("{:5f} {}".format(float(area),is_hukusu))