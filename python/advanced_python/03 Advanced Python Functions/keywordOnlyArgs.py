"""
argument를 키워드와 함께 받는 것을 (keyword=args) 의미한다.

def myFunction(arg1, arg2, arg3="foo")
myFection(1,2, arg3="bar")

def criticalFunc(arg1, suppressExc=False)
def criticalFunc(arg1, *,  suppressExc=False) 
    - separates positional argument form keyword only argument

"""

def myFunction(arg1, arg2, *, support=False):
    pass

def myFunction2(arg1, *args, support=False):
    print(arg1, *args, support)

def main():
    myFunction(1,2,support=True)
    myFunction2(1,23,4,2,3,support=True)
    myFunction2(1,23,4,2,3)


if __name__=="__main__":
    main()