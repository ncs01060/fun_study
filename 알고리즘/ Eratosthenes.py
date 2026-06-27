# 에라토스테네스의 체 구현
import math

num = int(input())

isPrime = [True] * (num + 1)
primeNumber = []

for i in range(2,int(math.sqrt(num))+1):
    if not isPrime[i]: continue
    for j in range(i*i,num+1,i):
        isPrime[j] = False
    

for i in range(2, num + 1):
    if isPrime[i]:
        primeNumber.append(i)
print(sum(primeNumber))

## 블로그에 적어야지