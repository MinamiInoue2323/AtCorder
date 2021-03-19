str_list = input()
now_index = 0

def is_dream(alist, index):
    print(alist[index:index+5])
    if(alist[index:index+5] == "dream"):
        return True
    else:
        return False
def is_erase(alist, index):
    print(alist[index:index+5])
    if(alist[index:index+5] == "erase"):
        return True
    else:
        return False

if len(str_list) < 5:
    print("NO")
    exit()


#make first flag
#make var dream true if it is dream, make false if it is erase
dream = False
if is_dream(str_list,now_index):
    dream = True
elif not is_erase(str_list,now_index):
    #print("pass")
    print("NO")
    exit()

if len(str_list) == 5:
    print("YES")
    exit()

while (now_index < len(str_list)):
    if dream:
        #now dream is true
        if str_list[now_index+5] == "d":
            now_index += 5
            continue
        elif str_list[now_index+5] == "e":
            nexts = [now_index+6]
            if nexts == "r":
                if str_list[now_index+7] == "e":
                    #so now it was dreamer
                    now_index += 7
                    if is_dream(str_list,now_index):
                        continue
                    elif is_erase(str_list,now_index):
                        dream = False
                        continue
                    else:
                        print("pass")
                        print("NO")
                        exit()
                elif str_list[now_index+7] == "a":
                    #so now it was eraser
                    now_index +=5
                    if is_dream(str_list,now_index):
                        dream = False
                        continue
                    else:
                        print("NO")
                        exit()
                else:
                    print("NO")
                    exit()  
            else:
                print("NO")
                exit()
        else:
            print("NO")
            exit()
    else:
        nexts = str_list[now_index+5]
        print(nexts)
        #now str is erase
        if nexts == "e":
            now_index += 5
            if is_erase(str_list,now_index):
                continue
            else:
                print("NO")
                exit()
        elif nexts == "d":
            now_index += 5
            if is_dream(str_list,now_index):
                dream = True
                continue
            else:
                print("NO")
                exit()
        elif nexts == "r":
            now_index += 6
            if is_dream(str_list,now_index):
                dream = True
                continue
            elif is_erase(str_list,now_index):
                continue
            else:
                print("NO")
                exit()



