```bash
$docker run -d -p 80:80 --name web webserver

$ docker ps -a
CONTAINER ID   IMAGE                   COMMAND                  CREATED          STATUS
PORTS                    NAMES
f38ab3a0b312   webserver               "/usr/sbin/apache2ct…"   4 seconds ago    Up 2 seconds
0.0.0.0:80->80/tcp       web

$curl localhost:80
TEST WEB
```