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

def greeting():
    yield 'Good mprning'