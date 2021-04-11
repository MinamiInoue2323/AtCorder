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

clist = "".join(fl) + "".join(letters - fl)

for guess in itertools.permutations(("0","1","2","3","4","5","6","7","8","9"), len(clist)):
  if "0" not in guess[:flen]:
    tt = testset.translate(str.maketrans(dict(zip(clist,guess))))
    tlist = tt.split()
    if int(tlist[0]) + int(tlist[1]) == int(tlist[2]):
      print(tlist[0])
      print(tlist[1])
      print(tlist[2])
      exit()

print("UNSOLVABLE")