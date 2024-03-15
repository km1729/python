"""
variable arguments are usfull when number of arguments are small
'*를 이용하면 리스트 받아 들 일 수 있다
'펑션을 불러올때도 '*를 빼먹지 않도록 한다
'*arg는 파라미터 중에 가장 뒤에 위치해야 한다
myfunction(base, *args): okay
myfunction(*base, args): error
"""

def addtion(*args):
    result = 0
    for arg in args:
        result += arg
    return result
    

def main():
    print(addtion(5, 10, 20, 30))
    print(addtion(1,2,3,4,5))

    myNums = [4,10,15,25]
    print(addtion(*myNums))


if __name__ == "__main__":
    main()