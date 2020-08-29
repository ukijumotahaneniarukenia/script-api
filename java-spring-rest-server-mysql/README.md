# java-spring-rest-server-mysql


- https://start.spring.io/


データベースの準備

```
$ su root

$ cd /usr/local/src/script-repo

$ bash ubuntu-18-04-install-mysql-8-X-X.sh

プロセスの実行ユーザーが登録されていることを確認
$ cat /etc/passwd | grep -i mysql
mysql:x:102:104:MySQL Server,,,:/var/lib/mysql:/bin/false

リハーサルではやさしく一つずつ実行 本番では思い切って実行
$ bash ubuntu-18-04-healthcheck-mysql-8-X-X.sh

プロセス確認

$ sudo lsof -i:3306 -P
COMMAND  PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
mysqld  6041 mysql   37u  IPv6 309758      0t0  TCP *:3306 (LISTEN)

軽く入って試し打ち

$ mysql -uuser01 -pMysql3306 -Dtestdb

mysql> select 'うんこ';
+-----------+
| うんこ    |
+-----------+
| うんこ    |
+-----------+
1 row in set (0.00 sec)

```

apiの確認とデータベースの確認

```
GET

$ mysql -uuser01 -pMysql3306 -Dtestdb

mysql> select * from employee;
+----+---------------+---------+
| id | name          | role    |
+----+---------------+---------+
|  1 | Bilbo Baggins | burglar |
|  2 | Frodo Baggins | thief   |
+----+---------------+---------+
2 rows in set (0.00 sec)


$ curl -X GET -s http://localhost:8080/api/all | jq
[
  {
    "id": 1,
    "name": "Bilbo Baggins",
    "role": "burglar"
  },
  {
    "id": 2,
    "name": "Frodo Baggins",
    "role": "thief"
  }
]

POST

$ curl -X POST -H 'Content-Type:application/json' localhost:8080/api/add -d'{"name":"まりこ","role":"Chef"}'
{"id":3,"name":"まりこ","role":"Chef"}
$ curl -X GET -s http://localhost:8080/api/all | jq
[
  {
    "id": 1,
    "name": "Bilbo Baggins",
    "role": "burglar"
  },
  {
    "id": 2,
    "name": "Frodo Baggins",
    "role": "thief"
  },
  {
    "id": 3,
    "name": "まりこ",
    "role": "Chef"
  }
]

$ mysql -uuser01 -pMysql3306 -Dtestdb

mysql> select * from employee;
+----+---------------+---------+
| id | name          | role    |
+----+---------------+---------+
|  1 | Bilbo Baggins | burglar |
|  2 | Frodo Baggins | thief   |
|  3 | まりこ        | Chef    |
+----+---------------+---------+
3 rows in set (0.00 sec)



NOTHING

$ curl -X GET -H 'Content-Type:application/json' -s localhost:8080/api/employees/5 | jq


GET

$ curl -X GET -H 'Content-Type:application/json' -s localhost:8080/api/employees/2 | jq
{
  "id": 2,
  "name": "Frodo Baggins",
  "role": "thief"
}

GET

$ curl -X GET -H 'Content-Type:application/json' -s localhost:8080/api/employees/3 | jq
{
  "id": 3,
  "name": "まりこ",
  "role": "Chef"
}


POST
$ curl -X PUT -H 'Content-Type:application/json' -s localhost:8080/api/employees/2 -d '{"name":"ぽるこ","role":"ぶた"}'
{"id":2,"name":"ぽるこ","role":"ぶた"}

$ curl -X GET -H 'Content-Type:application/json' -s localhost:8080/api/employees/2 | jq
{
  "id": 2,
  "name": "ぽるこ",
  "role": "ぶた"
}


$ mysql -uuser01 -pMysql3306 -Dtestdb

mysql> select * from employee;
+----+---------------+---------+
| id | name          | role    |
+----+---------------+---------+
|  1 | Bilbo Baggins | burglar |
|  2 | ぽるこ        | ぶた    |
|  3 | まりこ        | Chef    |
+----+---------------+---------+
3 rows in set (0.01 sec)


DELETE

$ curl -X DELETE -H 'Content-Type:application/json' -s localhost:8080/api/employees/2
{"id":2,"name":"ぽるこ","role":"ぶた"}
$ curl -X GET -H 'Content-Type:application/json' -s localhost:8080/api/employees/2 | jq

$ curl -X DELETE -H 'Content-Type:application/json' -s localhost:8080/api/employees/2
Could not find employee 2

$ mysql -uuser01 -pMysql3306 -Dtestdb


mysql> select * from employee;
+----+---------------+---------+
| id | name          | role    |
+----+---------------+---------+
|  1 | Bilbo Baggins | burglar |
|  3 | まりこ        | Chef    |
+----+---------------+---------+
2 rows in set (0.00 sec)
```


dockerホストからアクセスする際のURL

- http://172.17.0.2:8080/api/all


dockerコンテナからアクセスする際のURL

- http://localhost:8080/api/all


ポータブルな単一実行可能なjarファイルの作成

```

```
