N = int(input())
S = list(input())
Q = int(input())
query = []

def swap(a,b):
  tmp = S[a]
  S[a] = S[b]
  S[b] = tmp

for i in range(Q):
  qe = list(map(int,input().split()))
  query.append(qe)

swapc = 0

for qe in list(query):
  if qe[0] == 2:
    swapc += 1
  if qe[0] == 1:
    if swapc % 2 == 0:
      swap(qe[1] - 1, qe[2] - 1)
    else:
      a = 0
      b = 0
      if qe[1] <= N:
        a = qe[1] + N
      else:
        a = qe[1] - N

      if qe[2] <= N:
        b = qe[2] + N
      else:
        b = qe[2] - N
      swap(a-1, b-1)


if swapc % 2 == 0:
  print("".join(S))
else:
  print("".join(S[N:]) + "".join(S[:N]) )