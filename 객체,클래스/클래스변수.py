# 공통으로 사용되는 string, value
class Person():
    kind = "human"
    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()

# list 와 같은 자료구조에서는 주의 -> init 에서 초기화
class T():
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word("add 1")
c.add_word("add 2")
print(c.words)

d = T()
d.add_word("add A")
d.add_word("add B")
print(d.words)

# =================== 클래스 메소드, 스태틱 메소드 ===================== #
class Human:
    # class variable
    kind = "king"

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_ur_name(cls):
        return cls.kind

    @staticmethod
    def about():
        print("about human") # class 외부에 독립적으로 있는 메소드처럼 동작, self 없음 단, 클래스 내부에 사용되는 이유는 : human클래스에 연관된 메소드의 의미를 담고있다.

h1 = Human()
h2 = Human
print(h1)  # object = 객체 = human class 의 instance
print(h2)  # human class

# print(h1.x)
# print(h2.x)  # 접근x 에러
print(h1.what_is_ur_name())
print(h2.what_is_ur_name())  # object를 만들지 않아도 접근할 수 있다.
h2.about()
h1.about()

# =================== 특수 메소드 ===================== #
class Word:
    # __ 언더바 __ 에 해당하는 메소드 = 특수 메소드
    def __init__(self, text):
        self.word = text

    def __str__(self):  # 문자열 호출시 print()
        return " str sucess"

    def __len__(self):  # len() 호출시
        return len(self.word)

w = Word("test_text")
print(w)
print(len(w))  # = len(w.word)
