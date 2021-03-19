s = input()
str_list = [c for c in s]
is_odd = True

for i in str_list:
    ord_s = ord(i)
    if is_odd:
        if 65<=ord_s and ord_s <=90:
            print("No")
            exit()
        is_odd = False
    else:
        if 97<=ord_s and ord_s<=122:
            print("No")
            exit()
        is_odd = True
print("Yes")