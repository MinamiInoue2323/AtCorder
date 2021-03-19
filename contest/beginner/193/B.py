N = int(input())
shop_list = [list(map(int,input().split())) for _ in range(N)]
cost_list = []
for shop in shop_list:
    if (shop[2] - shop[0]) > 0:
        cost_list.append(shop[1])

if len(cost_list) == 0:
    print(-1)
else:
    print(min(cost_list))

#ソートで早くできるけどやり方わからんかった
        
    