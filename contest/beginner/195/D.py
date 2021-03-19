nums = list(map(int,input().split()))
N = nums[0]
M = nums[1]
Q = nums[2]
nimotsu = [list(map(int, input().split())) for _ in range(N)]
size, value = [list(i) for i in zip(*nimotsu)]
hako = list(map(int,input().split()))
query = [list(map(int, input().split())) for _ in range(Q)]
Qlist = [[0 for i in range(51)] for j in range(51)]

print(size)
print(value)
'''
print(nimotsu)
print(hako)
print(query)
print(Qlist)
'''

Qlist[0][0] = sum(value)
#print(value[:2])
#print(value[2:])
L = 50

while L > 0:
    R = 50
    now_score = sum(value[:R])
    Qlist[L][R] = now_score
    R = 49
    lostlist = sorted(value[R:])
    
    while R >= L:
        now_score += lostlist.pop()
        Qlist[L][R] = now_score
        R -= 1

    L -=1

