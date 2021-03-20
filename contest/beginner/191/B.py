N,X = map(int,input().split())
a_list = map(int,input().split())
ans_list = []

for a in a_list:
    if a != X:
        ans_list.append(str(a))

print(" ".join(ans_list))
        