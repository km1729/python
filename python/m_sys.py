import sys
# 인터프리터가 제공하는 변수과 함수를 직접 제어하기 위해 사용한다. 

# 입력받은 파라미터를 list형태로 읽어 올 수 있음
print(sys.argv)

myargv = sys.argv

for argv in myargv:
    print(argv)

