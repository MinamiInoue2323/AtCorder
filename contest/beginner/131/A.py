s = input()
a = [int(c) for c in s]
past = -5
for i in a:
    if past == i:
        print("Bad")
        exit()
    past = i
print("Good")


    