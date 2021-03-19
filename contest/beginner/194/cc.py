N = int(input())

num_list = list(map(int,input().split()))

print(num_list)
sum = 0

for x in num_list:
    sum +=x ** 2

for index, x in enumerate(num_list):
    
    #print(index)
    #print(x)
    for a in range(index + 1,N):
        sum += (x - num_list[a])**2
print(sum)