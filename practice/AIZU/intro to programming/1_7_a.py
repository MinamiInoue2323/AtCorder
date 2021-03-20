while 1:
    m,f,r = map(int,input().split())
    score = m + f
    if m == -1 and f == -1 and r == -1:
        break
    if m == -1 or f == -1:
        print("F")
    elif score >= 80:
        print("A")
    elif score >= 65:
        print("B")
    elif score >= 50:
        print("C")
    elif score >= 30:
        if r >= 50:
            print("C")
        else:
            print("D")
    else:
        print("F")
        