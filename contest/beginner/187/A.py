A,B = map(str,input().split())
alist = [int(x) for x in list(str(A))]
blist = [int(x) for x in list(str(B))]
print(max(sum(alist),sum(blist)))