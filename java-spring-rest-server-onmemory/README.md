# java-spring-rest-server-onmemory

- https://start.spring.io/

mavenタスクのプラグインのスプリングブートランを起動

8080ポートで起動
```
$ lsof -i:8080 -P
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
java    26744 aine   75u  IPv6 231214      0t0  TCP *:8080 (LISTEN)
```

api確認

```
GET

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


DELETE

$ curl -X DELETE -H 'Content-Type:application/json' -s localhost:8080/api/employees/2
{"id":2,"name":"ぽるこ","role":"ぶた"}
$ curl -X GET -H 'Content-Type:application/json' -s localhost:8080/api/employees/2 | jq
```

ポータブルな単一実行可能なjarファイルの作成

```
pom.xmlファイルが存在するディレクトリに移動
$ cd /home/aine/script-api/java-spring-rest-server-onmemory/payroll

ライフサイクルのパッケージをダブルクリックでも作成可能
$ ./mvnw package

実行ディレクトリにコピー
$ cp /home/aine/script-api/java-spring-rest-server-onmemory/payroll/target/payroll-0.0.1-SNAPSHOT.jar /home/aine/

実行ディレクトリに移動
$ cd /home/aine

実行
$ java -jar payroll-0.0.1-SNAPSHOT.jar
```
