instr = input()
keta = len(instr)
i = keta
count = 0
csum = 0

if i <=3:
    print(0)
    exit()

while i > 3:
    csum += (10**((count+1)*3) -10**(count*3)) * count
    i -= 3
    count += 1

csum +=(int(instr) + 1 - 10**(count*3)) * count

print(csum)

