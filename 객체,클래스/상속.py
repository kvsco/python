class Car:
    def __init__(self, model=None):
        self.model = model
        print("create Car")

    def run(self):
        print("car run ")


class Tesla(Car):
    def __init__(self, model='S series', auto_mode=False):
        # self.model = model
        super().__init__(model)
        self._auto_mode = auto_mode
        self.pwd = '123'

    @property
    def auto_mode(self):
        return self._auto_mode

    @auto_mode.setter
    def auto_mode(self, mode):
        if self.pwd == 'hidden key':
            self._auto_mode = mode
        else:
            print("Error")
            raise ValueError

    # 오버라이딩
    def run(self, pwd='123'):
        self.pwd = pwd
        print("tesla fast run")

    def auto_run(self):
        print("tesla car auto-run ")


class Benz(Car):
    pass


car = Car()
tesla = Tesla()
benz = Benz('E class')
print('car model :', car.model)
print('car model :', tesla.model)
print('car model :', benz.model)
print("#######")
tesla.run('hidden key')
tesla.auto_run()
benz.run()
print("#######")
# _ : 언더스코어 하나로 self 변수명을 숨길수는 있으나, 접근 가능 -->property
# __ : 외부에는 완전히 숨기는 경우, 단 클래스 내부에서는 호출되어 사용 가능
tesla.auto_mode = True  # property -> attributeError로 접근 불가, setter 설정
print(tesla.auto_mode)
