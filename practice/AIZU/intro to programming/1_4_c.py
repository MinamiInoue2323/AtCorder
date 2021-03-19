for i in range(20000):
    x,op,y = map(str,input().split())
    x = int(x)
    y = int(y)
    if op == "?":
        break
    ans = 0
    if op == "+":
        ans = x + y
    if op == "-":
        ans = x - y
    if op == "*":
        ans = x * y
    if op == "/":
        ans = x // y
    print(ans)
    