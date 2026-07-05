import time
def gcd(a:int,b:int):
    s = a%b
    if s != 0:
        return gcd(b,s)
    else:
        return b

a,b = map(int,input().split())
start = time.time()
print(gcd(a,b))
end = time.time()
print(f"{end - start:.5f}")