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

