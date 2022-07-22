# doc string 함수의 설명
def example_func(param1, param2):
    """
    Example function 의 기능은 'ㅇㅇㅇ'입니다.

    Args:
        param1: asdasd
        param2: asdasd
    Returns:
        bool: asdasd
    """
    return False

print(example_func.__doc__)

# inner function
def outer(a, b):

    def plus(c, d):  # 내부에서 여러번 호출되어 사용될 경우 사용
        return c+d

    r = plus(a, b)
    r2 = plus(b, a)
    r3 = plus(a+1, b+1)
    print(r)

outer(1, 2)

# 클로저
def outer1(a, b):
    def inner():
        return a + b

    return inner

f = outer1(3, 4) # 인수만 넣어두고 나중에 function 실행
print(f)
print(f())

def circle_area_func(pi):
    def area(rad):
        return pi * rad * rad

    return area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))

# 데코레이터 -> 함수에 대한 전후 처리를 반복적으로 하기 위함.
def print_info(func):
    def wrapper(*args, **kwargs):
        print(" start")
        print(f" func: {func.__name__}")
        print(f" args: {args}")
        print(f" kwargs: {kwargs}")
        res = func(*args, **kwargs)
        print(" end")
        return res
    return wrapper

@print_info
def add_num(a, b):
    return a + b

@print_info
def sub_num(a, b):
    return a - b

r = add_num(10,20)
r2 = sub_num(30,20)

# 람다
l = ['Mon', 'tue', 'weD', 'Thu', 'fri', 'sat', 'SUN']
def change_words(words, func):
    for word in words:
        print(func(word), end=",")
    print("")

sample_func = lambda x: x.capitalize()
change_words(l, sample_func)

change_words(l, lambda x: x.capitalize())
change_words(l, lambda x: x.lower())

# 제너레이터 --> 산출
g = ['Good morning', 'Good atfernoon', 'Good night']

for i in g:
    print(i)

print("################")

def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

# for g in greeting():
#     print(g)
gt = greeting()
c = counter()
print(next(gt))

print(next(c))
print(next(gt))

print(next(c))
print(next(gt))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

# list comprehension
t = (1,2,3,4,5)

r=[]
for i in t:
    r.append(i)

print(r)
r = [i for i in t if i % 2 == 0]  # 메모리, 처리속도가 빠르다는 장점 --> list를 사용하는 짧은 for 문
print(r)

r = []
t2 = (5,6,7,8,9,10)
for i in t:
    for j in t2:
        r.append(i*j)

print(r)

r = [i*j for i in t for j in t2]  # 단 2중포문의 경우, 가독성을 위해 그냥 기존 for문으로 작성하는게 보기에 좋다.
print(r)

# dict 내포
w = ['mon','tue','wed']
f = ['cofee','milk','water']

d={x:y for x,y in zip(w,f)}
print(d)

# 제너레이터 내포
gre = greeting()
gre = (i for i in range(10) if i % 2 == 0)  # tuple이 아닌 제너레이터 object 그자체
print(gre)

for x in gre:
    print(x)

# 변수 스코프
animal = 'cat'

def f():
    global animal
    print('first : ',animal)
    animal = 'dog'
    print('after : ', animal)
    print('locals : ', locals())  # 지역변수들
f()
print('global : ', animal)
print('globals : ', globals())  # 전역변수들
print('='*79)
# error handling
l = [1,2,3]
i = 5

try:
    l[i]
except IndexError as ie:
    print('dont-worry : ', ie)
except NameError as ne:
    print("error:", ne)
except Exception as e:
    print(f'unkwon errer:{e}')
else:  # except 없이 정상 동작 시
    print('-done-')
finally:  #반드시 실행
    print("clean.")
print('end prg')

# custom exception

class CustomError(Exception):  # 사용자가 정의하는 예외처리
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise CustomError(word)

check()