# 클래스, 초기화
s = 'dsfasdfafa'

print(s.capitalize())  # 드래그 -> goto -> declaration
print("="*60)
class Person(object):
    def __init__(self, name="홍길동"):
        self.name = name
        print("init person")

    def say_something(self):
        print(f"hello {self.name}")
        self.run(10)

    def run(self, num=5):
        print("run"*num)

    # 소멸자
    def __del__(self):
        print("delete instance")

person = Person()
person.say_something()

del person
print('#######')