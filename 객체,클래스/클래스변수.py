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

