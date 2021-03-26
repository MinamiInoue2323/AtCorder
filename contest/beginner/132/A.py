S = input()
str_dict = {}

for i in S:
    if i in str_dict.keys():
        str_dict[i] += 1
    else:
        str_dict[i] = 1

if len(str_dict) == 2:
    for i in str_dict.values():
        if i !=2:
            print("No")
            exit()
    print("Yes")
else:
    print("No")


