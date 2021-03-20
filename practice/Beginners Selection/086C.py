n = int(input())
plan_list=[]
for i in range(n):
    plan = list(map(int,input().split()))
    plan_list.append(plan)

start_x = 0
start_y = 0
start_time=0
for plan in plan_list:
    #print(plan)
    #print(plan[0])
    distance = abs((plan[1] - start_x) + (plan[2] - start_y))
    is_safe = distance - (plan[0] - start_time)
    if is_safe > 0 or is_safe % 2 == 1:
        print("No")
        exit()
    else:
        start_x = plan[1]
        start_y = plan[2]
        start_time = plan[0]
print("Yes")