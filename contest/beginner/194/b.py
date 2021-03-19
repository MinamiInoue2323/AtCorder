num_worker = int(input())

xy = [map(int, input().split()) for _ in range(num_worker)]
A, B = [list(i) for i in zip(*xy)]

#まず最小でかかる時間を求める
Amin =  [i for i, v in enumerate(A) if v == min(A)]
Bmin =  [i for i, v in enumerate(B) if v == min(B)]


#両方同じ人がやったほうがマシな場合
if len(Amin) == 1 and len(Bmin) == 1:
    Atime = A[Amin[0]]
    Btime = B[Bmin[0]]
    #print("Atime" + str(Atime))
    #print("Btime" + str(Btime))
    if Amin[0] == Bmin[0]:
        
        timesum = Atime + Btime
        nextminA = sorted(A)[1]
        nextminB = sorted(B)[1]
        if nextminA < timesum and nextminB < timesum:
            print(min(nextminA,nextminB))
        elif nextminA < timesum:
            print(nextminA)
        elif nextminB < timesum:
            print(nextminA)
        else:
            print(timesum)

    else:
        print(max(Atime,Btime))
elif len(Amin) > 1 :
    if len(Bmin) > 1:
        #A,B共に2以上
        Atime = A[Amin[0]]
        Btime = B[Bmin[0]]
        print(max(Atime,Btime))
    else:
        #Aが2つ以上でBが1
        Atime = A[Amin[0]]
        Btime = B[Bmin[0]]
        print(max(Atime,Btime))
else:
    #Aが1つでBが2以上
    Atime = A[Amin[0]]
    time = B[Bmin[0]]
    print(max(Atime,Btime))








