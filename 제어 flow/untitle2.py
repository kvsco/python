for word in ['my', 'name', 'is', 'yong']:
    if word == 'is':
        # break
        continue

    print(word)
# for else
for fruit in ['apple', 'orange', 'banana']:
    print(fruit)
    if fruit == 'banana':
        print('stop eating')
        break
else:
    print('ate all fruit')

# range()
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in num_list:
    print(i)

for i in range(2, 10, 3):  # start :2  end :10  step :3
    print(i)

for _ in range(10):  # under score -> 안쓰는 변수의 명시적인 의미
    print('hello')

# enumerate() -> index 를 함께 전달해줌
for i, fruit in enumerate(['appple', 'banana', 'orange']):
    print(i, fruit)

# zip()
days = ['mon', 'tue', 'wed']
fruits = ['appple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

# for i in range(len(days)):
#     print(days[i], fruits[i], drink[i])
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

# dict 의 for loop unpacking -> keys(), values(), items()
d = {'x': 100, 'y': 200}

for v in d.items():
    print(v)

for k, v in d.items():
    print(k, v)

# method define
def say_hello():
    say = 'hello'
    print("hello")
    return say

f = say_hello()
print(f"f = {f}")

num: int = 10
def add_num(a: int, b: int) -> int:
    return a+b

r1 = add_num(10,20)
r2 = add_num('a', 'b')
print(r1)
print(r2)

def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)

menu('beef','beer','ice')

# 명시적으로 파라미터 인수를 지정하는방법
menu(drink='ice', entree='beef', dessert='beer')

# default 인수
def menu2(entree='beef', drink='wine', dessert='icecream'):
    print(entree, drink, dessert)

menu2('chicken', drink="water")

# default 인수 사용시 주의점, list, dict 를 사용하지 않는다. python 의 특성 -> 참조 반환 object // 참조 반환 Obj를 꼭 써야한다면 None 으로 초기화
def func1(x, l=[]):
    l.append(x)
    return l

y = [1,2,3]
r = func1(100, y)
print(r)

def func2(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

# 여러개 인자값 사용 ---> *args (tuple)
def say_something(*args):
    print(args)
    for arg in args:
        print(arg)

say_something('hi','mike','nance')

# key word 인수 --> **kwargs (dict)
def k_menu(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(f"k : {k} , v : {v}")

k_menu(entree='beef', dessert='icecream', drink='coffee')

menu_dict = {
    'entree' : 'beef',
    'drink' : 'juice',
    'dessrt' : 'cake'
}
k_menu(**menu_dict)  # ** 의미 : dictionary -> unpacking 된다.

# 위치인수 args, kwargs 종합
def final_menu(name, *args, **kwargs):  # 순서 중요 * -> **
    print(f"name : {name}")
    print(f"apitzer : {args}")
    print(f"menu : {kwargs}")

final_menu("yong", 'choco', 'water', **menu_dict)
