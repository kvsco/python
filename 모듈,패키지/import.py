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

# import rule --> 알파벳 순서대로, 라이브러리 그룹묶음으로
# ================ 파이썬 표준라이브러리 ================
import collections
import os
import sys

# ================ 서드 파티 라이브러리 ================
# import pandas
# import termcolor

# ================ 패키지 모듈 ================
from example_package import utils

# ================ 로컬 파이썬 모듈 ================
import argv

print(collections.__file__)
# print(pandas.__file__)
# print(utils.__file__)
print(argv.__file__)

print(sys.path) # import 시 , 가능한 경로를 확인할 수 있다. 여기에 포함되는 경로에 모듈,패키지 위치
