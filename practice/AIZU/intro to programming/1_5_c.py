while 1:
    H,W = map(int,input().split())
    if W == 0 and H == 0:
        exit()

    for i in range(H):
        if i % 2 == 0:
            for i in range(W):
                if i % 2 == 0:
                    print("#",end="")
                else:
                    print(".",end="")
        else:
            for i in range(W):
                if i % 2 == 1:
                    print("#",end="")
                else:
                    print(".",end="")
        print()
    print()