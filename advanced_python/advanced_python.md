# Advanced python

[LinkedIn learning](https://www.linkedin.com/learning/advanced-python/strings-vs-bytes?autoSkip=true&autoplay=true&contextUrn=urn%3Ali%3AlyndaLearningPath%3A623b6345498ed46b03b56d47&resume=false&u=76793378)

## Summary

1. Python language features

   - Python coding style
     - PEP8 - Style guide for python code
     - code structure and format - import state go at the top, indent using spaces not tab, limilt lines 79 character (72 for doc-strings)
     - white space conventions
   - Truth value -
   - String vs bytes -
     - 두개를 같이 프린트(print(string+byte) 할 수없다. 두개를 같이 쓸려면 코드를 encode or decode해줘야한다.
   - Template strings
     - template 이라는 모듈? 라이브러리를 추가해서 템플릿 형태로 데이터를 출력할 수 있음

2. Built-in Functions  
    - Utilities - any, all, min, max, sum
    - Iterators - iter리스트 넥스트 사용가능, enumurate 인덱스 가져옴, zip 두개의 같은 길이 자료를 페어로 묶어줌, 딕셔너리만들 수 있음
    - Transforms - filter(함수, iterable) - 필터에 맞는 True값 반환, map(함수, iterable) - 리스트나, 튜플에 함수가 적용됨 맵 오브젝트로 반환 되기 때문에 대부분 앞에 list를 붙여서 사용
    - Itertools - 모듈을 불러와서 사용할 수 있다, count, cycle을 사용시 무제한으로 리스트를 출력할 수 있다. 이외에도 accumulate(), dropwhile()과 같은 명령어 사용가능

3. Advanced Python Functions  
    - Function doc strings: function, classes 모듈에 독 스트링스를 추가한다 
      - Enclose docstrings in triple quotes
      - First line should be summary sentence of functionality
      - Modules: List important classes, functions, exceptions
      - Classes: List important methods
      - Functions: List parameters and explain each, one per line, If there's a return value, then list it(other wise omit), If the function raises exceptions, mention those
      - https://www.python.org/dev/peps/pep-0257
    - Variable argument lists: allow high degree flexbility by accepting different numbers of parameters
      - 'using * to get a list of arguments
    - Lambda functions: small functions lambda (parameters) : (expression)
    - Keyword-only arguments: argument is specified by keyword myfunction(arg1, *,support=True)

4. Advanced Collections
    - python data type 
      - list: Mutable sequence of values
      - tuple: Fixed sequence of values
      - set: Sequence of distinct values
      - dictionary: collection of key-value pairs
      - [collections module](https://docs.python.org/3/library/collections.html)
        - namedtuple: maintainable and easy to read, lightweight immutable class, include useful methods
        - defalutdict: 리스트에서 중복되는 값들의 키와 갯수를 딕셔너리로 만드는 코드를 간단하게 작성 할 수 있다
        - orderedDict 
        - counter
        - deque

5. Advanced Classes and Objects

6. Using Logging

7. Python Comprehensions