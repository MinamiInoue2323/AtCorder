I,J = map(int,input().split())
a_array=[]

for i in range(I):
    line = list(map(int,input().split()))
    a_array.append(line)

b_array =[]

for i in range(J):
    b_array.append(int(input()))

for i in range(I):
    line_sum  = 0
    for j in range(J):
        line_sum += a_array[i][j]*b_array[j]
    print(line_sum)