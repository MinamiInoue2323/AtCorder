N,X = map(int, input().split())
bound_list = list(map(int, input().split()))


count = 1
now_place = 0

for i in bound_list:
    now_place += i
    if now_place <= X:
        count += 1
    else:
        break

print(count)
    