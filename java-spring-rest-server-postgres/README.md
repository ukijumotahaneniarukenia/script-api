# java-spring-rest-server-postgres

- https://start.spring.io/

データベースの準備

```
$ su root

$ cd /usr/local/src/script-repo

$ bash ubuntu-18-04-install-postgres-12-4.sh

プロセスの実行ユーザーが登録されていることを確認
$ cat /etc/passwd | grep -i postgres

登録されていない場合は登録

$ bash ubuntu-18-04-install-default-user.sh 1001 postgres 1001 postgres postgres_pwd

$ cat /etc/passwd | grep -i postgres
postgres:x:1001:1001::/home/postgres:/bin/bash


リハーサルではやさしく一つずつ実行 本番では思い切って実行
$ bash ubuntu-18-04-healthcheck-postgres-12-X.sh

プロセス確認

$ sudo lsof -i:5432 -P
COMMAND    PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
postgres 17801 postgres    3u  IPv4 388718      0t0  TCP localhost:5432 (LISTEN)

軽く入って試し打ち

$ psql -U postgres -d testdb
psql (12.4)
Type "help" for help.

testdb=# select 'うんこ';
 ?column? 
----------
 うんこ
(1 row)

```


apiの確認とデータベースの確認

```

GET

$ psql -U postgres -d testdb

testdb=# select * from employee;
 id |     name      |  role   
----+---------------+---------
  1 | Bilbo Baggins | burglar
  2 | Frodo Baggins | thief
(2 rows)


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

$ psql -U postgres -d testdb

testdb=# select * from employee;
 id |     name      |  role   
----+---------------+---------
  1 | Bilbo Baggins | burglar
  2 | Frodo Baggins | thief
  3 | まりこ        | Chef
(3 rows)



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


$ psql -U postgres -d testdb

testdb=# select * from employee;
 id |     name      |  role   
----+---------------+---------
  1 | Bilbo Baggins | burglar
  3 | まりこ        | Chef
  2 | ぽるこ        | ぶた
(3 rows)


DELETE

$ curl -X DELETE -H 'Content-Type:application/json' -s localhost:8080/api/employees/2
{"id":2,"name":"ぽるこ","role":"ぶた"}
$ curl -X GET -H 'Content-Type:application/json' -s localhost:8080/api/employees/2 | jq

$ curl -X DELETE -H 'Content-Type:application/json' -s localhost:8080/api/employees/2
Could not find employee 2

$ psql -U postgres -d testdb

testdb=# select * from employee;
 id |     name      |  role   
----+---------------+---------
  1 | Bilbo Baggins | burglar
  3 | まりこ        | Chef
(2 rows)

```



dockerホストからアクセスする際のURL

- http://172.17.0.2:8080/api/all


dockerコンテナからアクセスする際のURL(dockerコンテナにfirefoxなどのブラウザをインストールしておく)

- http://localhost:8080/api/all


ポータブルな単一実行可能なjarファイルの作成

```
pom.xmlファイルが存在するディレクトリに移動
$ cd /home/aine/script-api/java-spring-rest-server-postgres/payroll

ライフサイクルのパッケージをダブルクリックでも作成可能
$ ./mvnw package

実行ディレクトリにコピー
$ cp /home/aine/script-api/java-spring-rest-server-mysql/payroll/target/payroll-0.0.1-SNAPSHOT.jar /home/aine/

実行ディレクトリに移動
$ cd /home/aine

実行
$ java -jar payroll-0.0.1-SNAPSHOT.jar

```

