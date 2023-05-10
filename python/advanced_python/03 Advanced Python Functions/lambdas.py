"""
함수를 한줄로 간단하게 만들어 준다
lambda (parameter) : (expression)

"""



def CelsisusToFaharenheit(temp):
    return (temp * 9/5) +32

def FahrenheitToCelsisus(temp):
    return (temp-32) * 5/9


def main():
    ctmeps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    print(list(map(CelsisusToFaharenheit, ctmeps)))
    print(list(map(FahrenheitToCelsisus, ftemps)))


    # Lambda
    print("\n====lambda====")
    print(list(map(lambda t: (t * 9/5) +32, ctmeps)))
    print(list(map(lambda t: (t-32) * 5/9 , ftemps)))
    

if __name__=="__main__":
    main()