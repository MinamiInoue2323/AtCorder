# nまでの素数を表示させるプログラム

def sieve_of_eratosthenes(n): #エラトステネスのふるい
    candidate = list(range(2, n+1)) #候補
    prime = []
    limit = n**0.5 + 1 #+1がないと平方数を素数にしてしまう

    while True:
        p = candidate[0] 
        if limit <= p:
            prime.extend(candidate) #この時点での残っているのは素数
            break
        prime.append(p) #pを素数リストに登録

        candidate = [i for i in candidate if i % p != 0]


    return prime

n = int(input())

count = 0

prime = sieve_of_eratosthenes(n)

for i in prime:
    num = i ** 2
    while num <= n:
        #print("num:{}".format(num))
        count+=1
        num *= i


print(n - count)
        

