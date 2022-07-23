# import 폴더명.모듈명 (풀패키지)
# import example_package.utils
# from example_package.utils import say_twice -> 패키지 특정 함수, 잘 사용하지 않음
from example_package import utils
from example_package import utils as u  # 헷갈릴수 있기때문에 별로 추천하지 않음
from example_package.talk import song


# r = example_package.utils.say_twice('hello')
r = utils.say_twice('hello')
r = u.say_twice('bye')

print(r)
print(song.sing())
