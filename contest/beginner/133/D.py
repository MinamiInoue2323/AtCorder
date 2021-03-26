N = int(input())
dams = list(map(int,input().split()))

a = sum(dams)
i = 1
while i < N-1:
    a -= dams[i]*2
    i += 2
print(a,end="")

i = 1
past = a
while i < N:
    past = 2 * (dams[i-1] - past // 2)
    print(" {}".format(past),end="")
    i += 1
print()