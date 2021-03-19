a = list(map(int,input().split()))
kokei = a[0]+a[1]
shibou = a[1]

if kokei >= 15 and shibou >= 8:
    print(1)
elif kokei >= 10 and shibou >= 3:
    print(2)
elif kokei >= 3:
    print(3)
else:
    print(4)