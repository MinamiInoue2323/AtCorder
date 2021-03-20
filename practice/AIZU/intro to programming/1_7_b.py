while 1:
    n,x = map(int,input().split())
    if n == 0 and x == 0:
        break

    count = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if i+j+k == x:
                    if i != j and i != k and j != k:
                        pass
                    else:
                        count+=1
    print(count / 6)



