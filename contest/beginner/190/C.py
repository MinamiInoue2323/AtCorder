N,M = map(int,input().split())
dish_list = [False] * N
condition_list = []
for i in range(M):
    condition = list(map(int,input().split()))
    condition_list.append(condition)

K = int(input())
people_list = []
for i in range(K):
    person = list(map(int,input().split()))
    people_list.append(person)

pattern = 0
end = 2**K
#print(end)
maxcount = 0
while pattern != end:
    #print("pass")
    dish_list = [False] * N
    for i in range(K):
        if pattern >> i & 1:
            dish_list[people_list[i][1]-1] = True
        else:
            dish_list[people_list[i][0]-1] = True
    #print(dish_list)
    count = 0
    for condition in condition_list:
        if dish_list[condition[0]-1] and dish_list[condition[1]-1]:
            count += 1
    #print(count)
    maxcount = max(maxcount,count)
    pattern+=1

print(maxcount)



