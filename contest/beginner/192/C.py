N,K = map(str, input().split())
for i in range(int(K)):
    Nlist = [c for c in str(N)]
    Nlist.sort()
    small = Nlist
    large = list(reversed(Nlist))
    #print(small)
    #print(large)
    N = str(int("".join(large)) - int("".join(small)))
    if N == 0:
        print("0")
        exit()
print(N)

    
    
