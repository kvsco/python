import builtins

# print(globals())
# 내장함수
# https://docs.python.org/ko/3/library/functions.html

builtins.print()

ranking = {
    'A': 100,
    'B': 50,
    'C': 75
}

for i in ranking:
    print(i)
print("="*79)
print(ranking.get('A'))
print(ranking.get)
print(sorted(ranking, key=ranking.get, reverse=True))


## 라이브러리
# https://docs.python.org/ko/3/library/index.html
s = 'dsfadfafafaserdf'

d = {}
for i in s:
    if i not in d:
        d[i] = 0
    d[i] += 1
print(d)

from collections import defaultdict

d2 = defaultdict(int)
print(d2)
for i in s:
    d2[i] +=1
print(d2)
