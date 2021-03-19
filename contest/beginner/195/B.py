
a = list(map(int,input().split()))

ming = a[0]
maxg = a[1]

W = a[2]*1000

minmikan = W / maxg
maxmikan = W / ming

int_min = int(minmikan)
int_max = int(maxmikan)

if minmikan % 1 == 0:
    print("{} {}".format(int_min, int_max))
elif int(minmikan) == int(maxmikan):
    print("UNSATISFIABLE")
else:
    print("{} {}".format(int_min+1, int_max))