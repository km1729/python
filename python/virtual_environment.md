
1. 가상환경 package 설치  
    ``` bash
    sudo apt install python3.10-venv
    ```  

1. 가상환경 설치할 프로젝트 디렉토리로 이동 후 가상환경 생성

    ``` bash
    python3 -m venv venv
    python3 -m venv venv --system-site-packages #system levl package include
    ```  
    프로젝트 폴더 안에 가상환경 venv 폴더가 생성되고 코드 실행 시 가상환경을 인터프리터로 읽어준다.  

2. 가상환경 활성화 / 비활성화
    ``` bash
    source ./venv/bin/activate
    deactivate
    ```

3. 가상환 경 내 필요한 package 설치 - 개별설치
    ``` bash
    pip install package
    ```

    설치 된 패키지 목록 확인 및 txt 파일로 내보내기
    ``` bash
    pip freeze
    pip freeze > requirements.rxt
    ```

3. 가상환 경 내 필요한 package 설치 - requirements.txt 이용
    ``` bash
    
    pip install -r requirements.txt
    
    ```