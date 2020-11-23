データ準備
```
drop table if exists employee;

create table employee(id int,name varchar(100),role varchar(100));

insert into employee(id,name,role)values(1,'プリン','ポケモン');

insert into employee(id,name,role)values(2,'うんこ','糞');

select * from employee;
```

全件取得

```
$ curl -s -X GET -H 'application/json' 'http://localhost:4567/users/list'|jq
[
  {
    "id": 1,
    "name": "まるこ",
    "role": "ちびまるこ"
  },
  {
    "id": 2,
    "name": "ぽるこ",
    "role": "ブタ"
  },
  {
    "id": 3,
    "name": "ジーナ",
    "role": "恋人"
  }
]
```

単一取得

```
$ curl -s -X GET -H 'application/json' 'http://localhost:4567/users/get/1'|jq
{
  "id": 1,
  "name": "まるこ",
  "role": "ちびまるこ"
}
```

作成

```
$ curl -s -X POST -H 'application/json' 'http://localhost:4567/users/create' -d '{"name":"スカイツリー","role":"シンボル"}'|jq
[
  {
    "id": 1,
    "name": "まるこ",
    "role": "ちびまるこ"
  },
  {
    "id": 2,
    "name": "うんこ",
    "role": "マスコット"
  },
  {
    "id": 3,
    "name": "ジーナ",
    "role": "恋人"
  },
  {
    "name": "スカイツリー",
    "role": "シンボル",
    "id": 534632614
  }
]
```

更新

```
$ curl -s -X PATCH -H 'application/json' 'http://localhost:4567/users/update/534632614' -d '{"name":"うんこ","role":"マスコット"}'|jq
[
  {
    "id": 1,
    "name": "まるこ",
    "role": "ちびまるこ"
  },
  {
    "id": 2,
    "name": "うんこ",
    "role": "マスコット"
  },
  {
    "id": 3,
    "name": "ジーナ",
    "role": "恋人"
  },
  {
    "name": "うんこ",
    "role": "マスコット",
    "id": 534632614
  }
]
```

削除

```
$ curl -s -X DELETE -H 'application/json' 'http://localhost:4567/users/delete/831240579' | jq
[
  {
    "id": 1,
    "name": "まるこ",
    "role": "ちびまるこ"
  },
  {
    "id": 2,
    "name": "ぽるこ",
    "role": "ブタ"
  },
  {
    "id": 3,
    "name": "ジーナ",
    "role": "恋人"
  }
]
```
