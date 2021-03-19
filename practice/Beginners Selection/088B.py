N = input()
a = list(map(int,input().split()))
a.sort(reverse=True)

alice=0
bob=0


for index,i in enumerate(a):
    if index % 2 == 0:
        alice += i
    else:
        bob += i

print(alice - bob)

