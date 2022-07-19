# if 조건문
# indentationError 주의 -> 띄어쓰기 indent 주의
x = 0

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('its ten')
else:
    print('positive')

a = 5
b = 10
if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

# 논리연산자
a = 1
b = -1
print(a == b)
print(a != b)
print(a > 0 and b > 0)
print(a > 0 or b > 0)

# in & not
y = [1, 2, 3]
x = 1

if x in y:
    print('x in y')

if 100 not in y:
    print('100 not in')

a = 1
b = 2
if not a == b:  # ->  a != b 으로 쓰는게 나아보임
    print("a b equal®")

is_bool = True

if not is_bool:
    print('false')
else:
    print('true')

# 값 판정 테크닉
is_ok = True
is_ok = 1
is_ok = 0
is_ok = 1231230
is_ok = ''
is_ok = 'string'
is_ok = []
is_ok = [1, 2, 3]

if is_ok:  # False => 0, 0.0, '', [], (), {}, set()
    print("OK")
else:
    print("NO")

# None 판정 테크닉
is_empty = None
# print(help(is_empty))

# if is_empty == None: 논리 연산자 보다 'is' 사용
if is_empty is None:
    print('None !!')

print(1 == True) # 값 비교의 경우 연산자
# print(1 is True) # 오브젝트 비교의 경우

# 반복문
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("done")  # break 문을 만나면 else 문 출력되지 않음. 완전히 while 문 종료되어야 else 실행됨

count = 0
while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue  # 아래 print() 안찍힘

    print(count)
    count += 1

# input
while True:
    word = input('Enter:')
    if word == 'ok':
        break
    print('next')

# for loop = literate

some_list = [1, 2, 3, 4]
# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1
for i in some_list:
    print(i)
