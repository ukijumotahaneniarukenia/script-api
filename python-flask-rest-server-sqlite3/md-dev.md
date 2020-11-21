参考

- http://docs.peewee-orm.com/en/latest/

- http://docs.peewee-orm.com/en/latest/

事前準備

```
$ sudo apt install -y sqlite3


$ sqlite3 testdb
-- Loading resources from /home/aine/.sqliterc
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.

sqlite>>>.separator \t

sqlite>>>.import my-bookmark.tsv mybookmark

sqlite>>>select count(*) from mybookmark;
count(*)
----------
173

$ pip3 install --user flask


#ORMでmysqlとpostgresとsqlite3に対応できるぽい

- https://peewee.readthedocs.io/en/latest/peewee/database.html#using-sqlite

$ pip3 install --user peewee
```

サーバープロセス起動

```
$ python3 api.py
 * Serving Flask app "api" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:3000/ (Press CTRL+C to quit)
```

取得

CMD
```
$ curl -s -X GET -H 'Content-Type: application/json' http://0.0.0.0:3000/MyBookmark/get/1 | jq
{
  "status": 0,
  "param": {
    "id": 1
  },
  "result": {
    "id": 1,
    "url": "https://github.com/ukijumotahaneniarukenia",
    "title": "Github ukijumotahaneniarukenia"
  }
}
```

OUT

```
{
  "data": {
    "id": 1,
    "idgroup": 17,
    "url": "https://github.com/ukijumotahaneniarukenia"
  },
  "result": true
}
```


登録

CMD

```
$ curl -s -X POST -H 'Content-Type: application/json' http://0.0.0.0:3000/MyBookmark/create -d '{"url":"http://localhost","title":"うんこ"}' | jq
```

OUT

```
{
  "status": 0,
  "result": {
    "id": 3328548806,
    "url": "http://localhost",
    "title": "うんこ"
  }
}
```

POST

```
$ curl -s -X GET -H 'Content-Type: application/json' http://0.0.0.0:3000/MyBookmark/get/3328548806 | jq
{
  "status": 0,
  "param": {
    "id": 3328548806
  },
  "result": {
    "id": 3328548806,
    "url": "http://localhost",
    "title": "うんこ"
  }
}
```


更新

CMD

```
$ curl -s -X PATCH -H 'Content-Type: application/json' http://0.0.0.0:3000/MyBookmark/update/3328548806 -d '{"url":"http://localhost","title":"もりもり"}' | jq
```

OUT

```
{
  "status": 0,
  "param": {
    "id": 3328548806
  },
  "result": {
    "id": 3328548806,
    "url": "http://localhost",
    "title": "もりもり"
  }
}
```

POST

```
$ curl -s -X GET -H 'Content-Type: application/json' http://0.0.0.0:3000/MyBookmark/get/3328548806 | jq
{
  "status": 0,
  "param": {
    "id": 3328548806
  },
  "result": {
    "id": 3328548806,
    "url": "http://localhost",
    "title": "もりもり"
  }
}
```


削除

CMD

```
$ curl -s -X DELETE -H 'Content-Type: application/json' http://0.0.0.0:3000/MyBookmark/delete/3328548806 | jq
```

OUT

```
{
  "status": 0,
  "param": {
    "id": 3328548806
  }
}
```

POST

```
$ curl -s -X GET -H 'Content-Type: application/json' http://0.0.0.0:3000/MyBookmark/get/3328548806 | jq
{
  "status": 1,
  "message": "Traceback (most recent call last):\n  File \"/home/aine/.local/lib/python3.8/site-packages/peewee.py\", line 6860, in get\n    return clone.execute(database)[0]\n  File \"/home/aine/.local/lib/python3.8/site-packages/peewee.py\", line 4258, in __getitem__\n    return self.row_cache[item]\nIndexError: list index out of range\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File \"/home/aine/script-api/python-flask-rest-server-sqlite3/app.py\", line 26, in get_my_bookmark\n    my_bookmark = MyBookmark.get(MyBookmark.id == id)\n  File \"/home/aine/.local/lib/python3.8/site-packages/peewee.py\", line 6430, in get\n    return sq.get()\n  File \"/home/aine/.local/lib/python3.8/site-packages/peewee.py\", line 6863, in get\n    raise self.model.DoesNotExist('%s instance matching query does '\nMyBookmarkDoesNotExist: <Model: MyBookmark> instance matching query does not exist:\nSQL: SELECT \"t1\".\"id\", \"t1\".\"url\", \"t1\".\"title\" FROM \"mybookmark\" AS \"t1\" WHERE (\"t1\".\"id\" = ?) LIMIT ? OFFSET ?\nParams: [3328548806, 1, 0]\n"
}
```
