s = input()
str_list = s[::-1]
now_index = 0
def is_dream(alist, index):
    #print(alist[index:index+5])
    if(alist[index:index+5] == "maerd"):
        return True
    else:
        return False
def is_erase(alist, index):
    #print(alist[index:index+5])
    if(alist[index:index+5] == "esare"):
        return True
    else:
        return False
def is_eraser(alist, index):
    #print(alist[index:index+5])
    if(alist[index:index+6] == "resare"):
        return True
    else:
        return False
def is_dreamer(alist, index):
    #print(alist[index:index+5])
    if(alist[index:index+7] == "remaerd"):
        return True
    else:
        return False
def end():
    print("NO")
    exit()

while now_index < len(str_list):
    nstr = str_list[now_index]
    #print(nstr)
    if nstr == "m":
        if is_dream(str_list,now_index):
            now_index+=5
            continue
        else:
            end()
    if nstr == "r":
        nnstr = str_list[now_index+2]
        if nnstr == "s":
            if is_eraser(str_list,now_index):
                now_index+=6
                continue
            else:
                end()
        elif nnstr == "m":
            if is_dreamer(str_list,now_index):
                now_index+=7
                continue
            else:
                end()
        else:
            end()
    if nstr == "e":
        if is_erase(str_list,now_index):
            now_index+=5
            continue
        else:
            end()
    else:
        end()
print("YES")