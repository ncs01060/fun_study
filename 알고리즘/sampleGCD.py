import time,math
def gcd(a:int,b:int):
    while b != 0:
        a,b = b, a%b
    return a

a,b = map(int,input().split())

start = time.time()
print(gcd(a,b))
end = time.time()
print(f"{end - start:.5f}")


start = time.time()
# n부터 1까지 반복
for i in range(a, 0, -1):
    # a와 b가 동시에 나누어떨어지는 첫 번째 수가 최대 공약수
    if a % i == 0 and b % i == 0:
        print(i)
        # 최대 공약수를 구했기 때문에 빠져나옴
        break
end = time.time()
print(f"{end - start:.5f}")

start = time.time()
print(math.gcd(a,b))
end = time.time()
print(f"{end - start:.5f}")