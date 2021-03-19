
while 1:
    H,W = map(int,input().split())
    if W == 0 and H == 0:
        exit()

    for i in range(H):
        if i == 0 or i == H-1:
            print("#" * W)
        else:
            print("#"+"."* (W-2)+"#")
    print()
