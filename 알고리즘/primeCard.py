# 프로그래머스 소수찾기
from itertools import permutations

string = input()
num = list(string)
setlist = set()
for i in range(1,len(num)+1):

    temp = list(permutations(num,i))
    for i in temp:
        setlist.add(i)
word_list = []
s = ""
for i in setlist:
    for j in i:
        s += j
    word_list.append(int(s))
    s = ""


word_list = set(word_list)
isPrime = [True] * (max(word_list) + 1)
isPrime[0] = False
isPrime[1] = False

for i in range(2,int(max(word_list)*0.5)+1):
    if not isPrime[i]: continue
    for j in range(i*i,max(word_list)+1,i):
        isPrime[j] = False

count = 0
for i in word_list:
    print(f"{i} is {isPrime[i]}")
    if isPrime[i]:
        count+=1
print(count)
