class Person:
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age > 18:
            print("ok you can drive")
        else:
            raise Exception("nope you are so young!!")

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age=19):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

baby = Baby()
adult = Adult()
# baby.drive()
adult.drive()

class Car:
    def __init__(self, model=None):
        self.model = model
        print("create Car")

    def run(self):
        print("car run ")

    def drive(self, person):
        person.drive()

car = Car()
# car.drive(baby)
car.drive(adult)