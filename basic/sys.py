import sys
# 인터프리터가 제공하는 변수과 함수를 직접 제어하기 위해 사용한다. 
# 입력받은 파라미터를 list형태로 읽어 올 수 있다
# sys.argv
print(sys.argv)
for argv in sys.argv:
    print(argv)

# sys.path
# 경로를 추가하고 그 안에 있는 모듈을 사용할 수 있게 한다.
sys.path.append('/e/projects/python/basic')
import turtle


# sys.stdin, sys.stdout, sys.stderr

# input prompt가 나오고 한줄 씩 입력되고 출력됨
# for line in sys.stdin:
#     print(line)

sys.stdout.write("stdout: Hello World \n")

try:
    result = 1/0
except Exception as e:
    sys.stderr.write(f"오류 발생: {e}")

# get python version
print(f"python version: {sys.version} \n")

# get platform information
# 현재 실행 중인 시스템의 플랫폼을 나타낸다. 
print(f"platform: {sys.platform} \n")

print(f"기본 인코딩 방식: {sys.getdefaultencoding()} \n")
print(f"파일 인코딩 방식: {sys.getfilesystemencoding()} \n")

my_list = [1,2,3,4,5]
print(f"객체 참조회수: {sys.getrefcount(my_list)}")

sys.setrecursionlimit(100)
def recursive_func(n):
    if n == 0:
        return 0
    else:
        return recursive_func(n - 1) + 1

print(recursive_func(10))
print(f"디폴트 리커시브 리미트: {sys.getrecursionlimit()} \n")
# print(f"재귀 호출의 최대 깊이를 설정하는 함수: {sys.setrecursionlimit(10)}")