# 파일 생성 + 작성

f = open('test.txt', 'w')
f.write(" first txet open")
f.close()

# with statement
with open('test.txt', 'w+') as f:
    f.write("blah blah~")
    f.seek(0)
    print( f.read() )
