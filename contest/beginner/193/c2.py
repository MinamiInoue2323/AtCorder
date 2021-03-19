import math

n = int(input())


#print(int(n/math.sqrt(n)))

oklist=set()

for i in range(2,int(math.sqrt(n))+1):
    num = i * i
    #print("num:{}".format(num))
    while num <= n:
        
        if num not in oklist:
            #print(num)
            oklist.add(num)


        num *= i

print(n - len(oklist))