파이썬 패키지을 만들 수 있게 해주는 모듈이다.  
우리가 사용하고 있는 pandas, numpy 와 같은 외부 패키지들과 같이 내가 만드는 계산기 또는 이미지를 다운로드 받는 패키지 등을 만들고 공유할 수 있게 해주는 패키지이다.  

## 패키지를 생성하기 위해 필요한 것  
> my_package_dir    
> - \__init__.py  
> - setup.py  
> - my_code_dir
>     - \__init__.py
>     - myscript.py  
>   

위의 디렉토리와 파일들을 준비 한 후 아래의 명령어를 실행하면 패키지가 생성된다  
```bash
pip install .
```

패키지가 생성되면 같은 directory내에 **build**와 **packageName.egg-info**의 두개의 디렉토리가 생성된다.  

만들어진 패키지를 테스트 하기 위해서 파이썬을 실행하고 패키지를 불러와보자. 오..... 만들어진 패키지를 사용 할 수 있다.  감동  

```bash
Python 3.10.10 (main, Mar 21 2023, 18:45:11) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from km import calculator
>>> calculator.add(3,6)
9
>>> calculator.multiply(13345,23123)
308576435
>>> calculator.divide(43454354,2234234)
19.44932983742974
``` 

아래의 링크 중 유투브 링크를 보고 실습한 내용입니다.  

참고  
- [setuptools](https://setuptools.pypa.io/en/latest/userguide/index.html)  
- [An Overview of Packaging for Python](https://packaging.python.org/en/latest/overview/)  
- [Youtube - Python Setuptools Tutorial ](https://youtu.be/JKegib9jgVA)  