
while 1:
    H,W = map(int,input().split())
    if W == 0 and H == 0:
        exit()

    for i in range(H):
        print("#" * W)
    print()
