def gcd(a:int,b:int):
    s = a%b
    if s != 0:
        return gcd(b,s)
    else:
        return b

a,b = map(int,input().split())
print(gcd(a,b))