``` docker-compose up ```
실행 시 다음과 같이 두개의 컨테이너가 실행 된것을 확인할 수 있다.
local:8080으로 접속시 pgadmin으로 접속가능

포드맨 데스크탑에서 컨테이너 cli클릭시 psql로 접속 가능

```bash
psql -U postgres
```


pgadmin에서 포스트그레스로는 어떻게 연결하지?


포드맨을을 이용해서 pod를 먼저 생성하고
pod에 pgadmin이랑 postgresql을 추가하고 테스트한 포스트
https://techviewleo.com/how-to-run-postgresql-in-podman-container/

Reference:  
https://cheesecat47.github.io/programming/2021/03/07/PostgreSQL-Docker/