a,b,c = map(int,input().split())

tmp = 0
if a > b:
    tmp = a
    a = b
    b = tmp
if b > c:
    tmp = c
    c = b
    b = tmp
if a > b:
    tmp = a
    a = b
    b = tmp

print("{} {} {}".format(a,b,c))
