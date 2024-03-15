# docstring
# 함수, 클라스, 모듈을 설명을 추가 하는것.
# fucntion.__doc__ 를 이용해 description을 출력할 수 있다



def myFunction(arg1, arg2=None):
    """ myFunction(arg1, arg2=None) 

    Parameters:
    arg1: the first argument
    arg2: second argument
    """
    print(arg1, arg2)

def main():
    print(myFunction.__doc__)

if __name__=="__main__":
    main()