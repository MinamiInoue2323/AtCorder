N = int(input())
room_list=[[[0 for k in range(10)] for i in range(3)] for j in range(4)]

for i in range(N):
    b,f,r,v = map(int,input().split())
    room_list[b-1][f-1][r-1] += v

for i in range(4):
    if i != 0:
        print("####################")
    for j in range(3):
        for k in range(10):
            print(" {}".format(room_list[i][j][k]),end="")
        print()
        
