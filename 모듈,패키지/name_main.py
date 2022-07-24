import example_package.talk.song

print('name : ',__name__)

# test 목적의 스크립트 코딩 스타일
def main():
    print('main 실행')
    example_package.talk.song.sing()

if __name__ == "__main__":
    main()
