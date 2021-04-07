N = int(input())
alist = list(map(int,input().split()))
ans = [0] * N
#print(ans) 

now = N
ac = 0
aa = []
while now > 0:
  r = alist.pop()
  c = 0
  t = N // now

  for i in range(2,t+1):
    c += ans[i * now - 1]
  
  if c % 2 != r:
    ans[now - 1] = 1
    aa.append(str(now))
    ac += 1

  now -= 1
print(ac)
print(" ".join(aa))