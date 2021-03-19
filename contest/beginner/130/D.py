N,K = map(int, input().split())
num_list = list(map(int, input().split()))

count = 0
now_sum = 0

left = 0
right = 0
for i in range(N):
    while now_sum < K:
        if right == N:
            break
        else:
            now_sum += num_list[right]
            right += 1
    if now_sum < K:
        break
    count += N - right + 1
    now_sum -= num_list[left]
    left += 1

print(count)