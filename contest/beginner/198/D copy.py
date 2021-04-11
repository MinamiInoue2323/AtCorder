import itertools
A = input()
B = input()
C = input()

testset =" ".join([A,B,C])

words = "".join([A,B,C])
letters = set(words)


if len(letters) > 10:
  print("UNSOLVABLE")
  exit()

fl = set()
fl.add(A[0])
fl.add(B[0])
fl.add(C[0])
flen = len(fl)
flast = set()
flast.add(A[-1])
flast.add(B[-1])
flast.add(C[-1])



clist = "".join(fl) + "".join(letters - fl)
digits = ("0","1","2","3","4","5","6","7","8","9")

for guess in itertools.permutations(digits, len(flast)):
  tt = testset.translate(str.maketrans(dict(zip(flast,guess))))
  

  if "0" not in guess[:flen]:
    tt = tt.translate(str.maketrans(dict(zip(clist,guess))))
    a_d,b_d,c_d = map(str,tt.split())
    if a_d + b_d == c_d:
      print(a_d)
      print(b_d)
      print(c_d)
      exit()

print("UNSOLVABLE")