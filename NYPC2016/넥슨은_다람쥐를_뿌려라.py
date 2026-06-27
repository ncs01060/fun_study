n = int(input()) # nxn 배열 생성
border = [] # 배열 담을 변수
playerCount = 0 # 플레이어 수
for i in range(n): # 배열 입력
    line = input()
    t = []
    for i in line:
        if i == "C":
            playerCount += 1
        t.append(i)
    border.append(t)

if playerCount == 0: # 플레이어가 없다면 그대로 출력
    for i in range(n):
        for j in range(n):
            print(border[i][j],end="")
        print()

monsterCount = playerCount * 2 # 다람쥐 수 (플레이어 * 2)

for i in range(n): # 위에서부터 플레이어 수의 2배만큼 다람쥐 출력
    for j in range(n):
        if monsterCount > 0:
            print('D',end="")
            monsterCount-=1
        else:
            print(border[i][j],end="")
    print()


