a = int(input())

for i in range(1,a+1):
    if i % 3 == 0:
        print(" {}".format(i),end="")
    else:
        a =[int(j) for j in str(i)]
        if 3 in a:
            print(" {}".format(i),end="")
    