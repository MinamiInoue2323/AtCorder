a = list(map(int,input().split()))
N = a[0]
Y = a[1] / 1000

#1,5,10で作れるか
num_1 = int(Y % 5)

num_105 = N-num_1
if 10 * num_105 + num_1 < Y :
    print("-1 -1 -1")
    exit()

while num_1 <= N:
    
    for num_5 in range(num_105+1):
        
        #iは5の枚数
        num_10 = num_105 - num_5
        sum = num_10 * 10 + (num_5) * 5 + num_1 
        #print("test:{} {} {}".format(num_10,num_5,num_1))
        if sum < Y:
            break
        elif sum == Y:
            print("{} {} {}".format(num_10,num_5,num_1))
            exit()
    num_1 +=5
    num_105 = N-num_1
print("-1 -1 -1")

