A,B,C = map(int,input().split())

while 1:
    if C == 0:
        if A == 0:
            print("Aoki")
            exit()

        A -= 1
        C = 1
    else:
        if B == 0:
            print("Takahashi")
            exit()
        B -= 1
        C = 0
