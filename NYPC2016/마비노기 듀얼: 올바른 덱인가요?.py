n = int(input()) # 덱에 넣을 카드개수
dack = set() # 중복방지
for i in range(n): # 카드 입력
    temp = input()
    dack.add(temp)

if len(dack) > 3: # 서로다른 성질의 카드가 3개 이상이면 invalid
    print("invalid")
else:
    print("valid")