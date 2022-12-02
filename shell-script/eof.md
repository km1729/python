eof  = End of File로 파일을 업데이트 할때 사용된다.  
사용방법  
``` bash
cat <<eof > test.conf
> nameserver 168.126.63.1
> nameserver 168.126.63.2
> EOF
```
결과
```bash
(base) k@local:~/practices/shell-script$ cat test.conf 
nameserver 168.126.63.1
nameserver 168.126.63.2
```  
덮어쓰기  
``` bash
(base) k@local:~/practices/shell-script$ cat <<eof > test.conf
결과 덮어쓰기
eof
(base) k@local:~/practices/shell-script$ cat test.conf 
결과 덮어쓰기
```
이어쓰기  
```bash
(base) k@local:~/practices/shell-script$ cat <<eof >> test.conf
결과 이어쓰쓰기
eof
(base) k@local:~/practices/shell-script$ cat test.conf 
결과 덮어쓰기
결과 이어쓰쓰기
```
