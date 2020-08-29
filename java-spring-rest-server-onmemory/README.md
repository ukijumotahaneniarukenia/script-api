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
$ curl -X GET -s http://localhost:8080/employees | jq
{
  "_embedded": {
    "employeeList": [
      {
        "id": 1,
        "name": "Bilbo Baggins",
        "role": "burglar",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/1"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      },
      {
        "id": 2,
        "name": "Frodo Baggins",
        "role": "thief",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/2"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      }
    ]
  },
  "_links": {
    "self": {
      "href": "http://localhost:8080/employees"
    }
  }
}
```


POST

```
$ curl -X POST -H 'Content-Type:application/json' -s http://localhost:8080/employees -d '{"id":3,"name":"まりこ","role":"Chef"}'
{"id":3,"name":"まりこ","role":"Chef"}

$ curl -X GET -s http://localhost:8080/employees | jq
{
  "_embedded": {
    "employeeList": [
      {
        "id": 1,
        "name": "Bilbo Baggins",
        "role": "burglar",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/1"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      },
      {
        "id": 2,
        "name": "Frodo Baggins",
        "role": "thief",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/2"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      },
      {
        "id": 3,
        "name": "まりこ",
        "role": "Chef",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/3"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      }
    ]
  },
  "_links": {
    "self": {
      "href": "http://localhost:8080/employees"
    }
  }
}

```


PUT

```
$ curl -X PUT -H 'Content-Type:application/json' -s http://localhost:8080/employees/3 -d '{"name":"ぽるこ","role":"ぶた"}'
{"id":3,"name":"ぽるこ","role":"ぶた"}

$ curl -X GET -s http://localhost:8080/employees | jq
{
  "_embedded": {
    "employeeList": [
      {
        "id": 1,
        "name": "Bilbo Baggins",
        "role": "burglar",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/1"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      },
      {
        "id": 2,
        "name": "Frodo Baggins",
        "role": "thief",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/2"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      },
      {
        "id": 3,
        "name": "ぽるこ",
        "role": "ぶた",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/3"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      }
    ]
  },
  "_links": {
    "self": {
      "href": "http://localhost:8080/employees"
    }
  }
}
```


DELETE

```
$ curl -X DELETE -H 'Content-Type:application/json' -s http://localhost:8080/employees/3

$ curl -X GET -s http://localhost:8080/employees | jq
{
  "_embedded": {
    "employeeList": [
      {
        "id": 1,
        "name": "Bilbo Baggins",
        "role": "burglar",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/1"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      },
      {
        "id": 2,
        "name": "Frodo Baggins",
        "role": "thief",
        "_links": {
          "self": {
            "href": "http://localhost:8080/employees/2"
          },
          "employees": {
            "href": "http://localhost:8080/employees"
          }
        }
      }
    ]
  },
  "_links": {
    "self": {
      "href": "http://localhost:8080/employees"
    }
  }
}
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
