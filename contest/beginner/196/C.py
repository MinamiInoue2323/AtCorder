n = input()
num_len = len(n)
kaburi_keta = num_len // 2
count = 0
if num_len % 2 == 1:
    for i in range(kaburi_keta):
        count = count * 10 + 9
else:
    a = int(n[:kaburi_keta])
    b = int(n[kaburi_keta:])
    #print("{} {}".format(a,b))
    #small = min(a,b)
    #big = max(a,b)
    #saitei = int("1" + "0" * (kaburi_keta -1))

    if a > b:
        count +=a - 1
    elif a == b:
        count += a
    else:
        count += a
    #print(saitei)
    '''
    if small >= saitei:
        count += small
    else:
        count += big - 1
    '''

print(count)