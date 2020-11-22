from flask import Flask, jsonify, make_response, request, Response
import flask
import peewee
import traceback
import json
import random

db = peewee.SqliteDatabase('testdb')

class MyBookmark(peewee.Model):
    id = peewee.IntegerField()
    url = peewee.TextField()
    title = peewee.TextField()

    class Meta:
        database = db

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #日本語デコード
app.config['JSON_SORT_KEYS'] = False #デフォルトソートのまま

@app.route('/MyBookmark/get/<int:id>', methods=['GET'])
def get_my_bookmark(id):
  result = {}
  response_header = {}
  response_header['Access-Control-Allow-Origin'] = 'http://0.0.0.0:8080'
  response_header['Content-type'] = 'application/json; charset=utf-8'

  try:

    my_bookmark = MyBookmark.get(MyBookmark.id == id)

    result['status'] = 0
    result['message'] = 'select target item'

    param = {}
    param['id'] = id
    result['param'] = param

    data = {}
    data['id']=my_bookmark.id
    data['url']=my_bookmark.url
    data['title']=my_bookmark.title
    result['result'] = data
    return Response(headers=response_header, response=json.dumps(result), status=200)

  except Exception:

    result['status'] = 1
    result['message'] = traceback.format_exc()
    return Response(headers=response_header, response=json.dumps(result), status=404)

@app.route('/MyBookmark/create', methods=['POST'])
def create_my_bookmark():
  result = {}
  response_header = {}
  response_header['Access-Control-Allow-Origin'] = 'http://0.0.0.0:8080'
  response_header['Content-type'] = 'application/json; charset=utf-8'

  json_data = request.get_data()

  request_data = json.loads(json_data)

  target_id = random.sample(range(10000000000), 1)[0]
  target_url = request_data['url']
  target_title = request_data['title']

  try:
    target_item = MyBookmark.get(
      MyBookmark.id == target_id
    )
    result['status'] = 1
    param = {}
    param['id'] = target_id
    result['param'] = param
    result['message'] = 'already exists target item'
    # https://developer.mozilla.org/ja/docs/Web/HTTP/Status/409
    return Response(headers=response_header, response=json.dumps(result), status=409)
  except Exception:
    target_item = None

  if target_item is None:
    try:
      MyBookmark.insert(id=target_id,url=target_url,title=target_title).execute()
      result['status'] = 0
      result['message'] = 'create target item'
      data = {}
      data['id']=target_id
      data['url']=target_url
      data['title']=target_title
      result['result'] = data
      # https://developer.mozilla.org/ja/docs/Web/HTTP/Status/201
      return Response(headers=response_header, response=json.dumps(result), status=201)
    except Exception:

      result['status'] = 1
      result['message'] = traceback.format_exc()
      # https://developer.mozilla.org/ja/docs/Web/HTTP/Status/500
      return Response(headers=response_header, response=json.dumps(result), status=500)


#フレームワークごとにリクエストメソッドの使い勝手ないしは意味の通り具合とうまく折り合いをつけるのがよさそうだ
#https://stackoverflow.com/questions/53611800/how-handle-patch-method-in-flask-route-as-api
@app.route('/MyBookmark/update/<int:id>', methods=['PATCH','OPTIONS'])
def update_my_bookmark(id):
  result = {}
  response_header = {}
  response_header['Access-Control-Allow-Origin'] = 'http://0.0.0.0:8080'
  response_header['Access-Control-Allow-Methods'] = 'PATCH, OPTIONS'
  response_header['Content-type'] = 'application/json; charset=utf-8'

  if flask.request.method == 'OPTIONS':
    # プリフライトリクエスト対応
    target_item = MyBookmark.get(
      MyBookmark.id == id
    )
    if not target_item is None:
      return Response(headers=response_header, response=json.dumps(result), status=200)
    else:
      result['status'] = 1
      result['message'] = 'not exists target item'
      param = {}
      param['id'] = id
      result['param'] = param
      return Response(headers=response_header, response=json.dumps(result), status=404)
  else:
    # プリフライトリクエスト後のリクエスト対応
    json_data = request.get_data()
    request_data = json.loads(json_data)

    try:
      target_item = MyBookmark.get(
        MyBookmark.id == id
      )
      target_item.url = request_data['url']
      target_item.title = request_data['title']

      target_item.save()

      result['status'] = 0
      result['message'] = 'update target item'

      param = {}
      param['id'] = id
      result['param'] = param

      data = {}
      data['id']=id
      data['url']=target_item.url
      data['title']=target_item.title
      result['result'] = data
      return Response(headers=response_header, response=json.dumps(result), status=200)
    except Exception:
      result['status'] = 1
      result['message'] = traceback.format_exc()
      return Response(headers=response_header, response=json.dumps(result), status=500)

#https://stackoverflow.com/questions/22181384/javascript-no-access-control-allow-origin-header-is-present-on-the-requested
@app.route('/MyBookmark/delete/<int:id>', methods=['DELETE','OPTIONS'])
def delete_my_bookmark(id):
  result = {}
  response_header = {}
  response_header['Access-Control-Allow-Origin'] = 'http://0.0.0.0:8080'
  response_header['Access-Control-Allow-Methods'] = 'DELETE, OPTIONS'
  response_header['Content-type'] = 'application/json; charset=utf-8'

  if flask.request.method == 'OPTIONS':
    # プリフライトリクエスト対応
    target_item = MyBookmark.get(
      MyBookmark.id == id
    )
    if not target_item is None:
      return Response(headers=response_header, response=json.dumps(result), status=200)
    else:
      result['status'] = 1
      result['message'] = 'not exists target item'
      param = {}
      param['id'] = id
      result['param'] = param
      return Response(headers=response_header, response=json.dumps(result), status=404)
  else:
    # プリフライトリクエスト後のリクエスト対応
    try:
      target_item = MyBookmark.get(
        MyBookmark.id == id
      )
    except Exception:
      target_item = None
      param = {}
      param['id'] = id
      result['status'] = 1
      result['param'] = param
      result['message'] = 'not exists target item'
      return Response(headers=response_header, response=json.dumps(result), status=404)

    if not target_item is None:

      try:

        MyBookmark.delete_instance(target_item)
        result['status'] = 0
        result['message'] = 'delete target item'
        # https://developer.mozilla.org/ja/docs/Web/HTTP/Status/204
        return Response(headers=response_header, response=json.dumps(result), status=204)

      except Exception:
        result['status'] = 1
        result['message'] = traceback.format_exc()
        return Response(headers=response_header, response=json.dumps(result), status=500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
