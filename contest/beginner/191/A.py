V,T,S,D = map(int,input().split())

start_vanish = V * T
end_vanish = V * S

if D < start_vanish or D > end_vanish:
    print("Yes")
else:
    print("No")