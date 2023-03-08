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

1. Built-in Functions
   - Utilities - any, all, min, max, sum
   - Iterators - iter리스트 넥스트 사용가능, enumurate 인덱스 가져옴, zip 두개의 같은 길이 자료를 페어로 묶어줌, 딕셔너리만들 수 있음
   - Transforms - filter(함수, iterable) - 필터에 맞는 True값 반환, map(함수, iterable) - 리스트나, 튜플에 함수가 적용됨 맵 오브젝트로 반환 되기 때문에 대부분 앞에 list를 붙여서 사용
   - Itertools - 모듈을 불러와서 사용할 수 있다, count, cycle을 사용시 무제한으로 리스트를 출력할 수 있다. 이외에도 accumulate(), dropwhile()과 같은 명령어 사용가능
