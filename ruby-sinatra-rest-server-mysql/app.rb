require 'sinatra'
require 'sinatra/cross_origin'
require 'json'

UPLOAD_DIR_NAME = 'upload'

my_data = <<"MY_JSON"
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
MY_JSON

my_data_list = JSON.load(my_data)

configure do
  enable :cross_origin
end

options '*' do
  response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, PUT'
  response.headers['Access-Control-Allow-Headers'] = 'Content-Disposition'
  response.headers['Access-Control-Allow-Origin'] = 'http://0.0.0.0:8000'
  200
end

get '/users/list' do
  my_data
end

get '/users/get/:id' do
  result = {}
  my_data_list.map{|e|
    if e['id'] == params['id'].to_i
      result = e
    end
  }
  result.to_json
end

post '/users/create' do
  body = request.body.read
  hash = JSON.parse(body)
  hash['id'] = rand(1..1_000_000_000)
  my_data_list.push(hash)
  my_data_list.to_json
end

patch '/users/update/:id' do
  body = request.body.read
  request_param = JSON.parse(body)
  my_data_list.map{|e|
    if e['id'] == params['id'].to_i
      e['name'] = request_param['name']
      e['role'] = request_param['role']
    end
  }
  my_data_list.to_json
end

delete '/users/delete/:id' do
  my_data_list.map{|e|
    if e['id'] == params['id'].to_i
      my_data_list.delete(e)
    end
  }
  my_data_list.to_json
end

post '/users/upload' do
  # POSTはレスポンスヘッダいらない
  if params[:image] && params[:image][:filename]
    filename = params[:image][:filename]
    file = params[:image][:tempfile]
    path = "./upload/#{filename}"
    Dir.mkdir(UPLOAD_DIR_NAME) unless Dir.exist?(UPLOAD_DIR_NAME)
    File.open(path, 'wb') do |f|
      f.write(file.read)
    end
  end
  200
end

put '/users/upload' do
  response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, PUT'
  response.headers['Access-Control-Allow-Headers'] = 'Content-Disposition'
  response.headers['Access-Control-Allow-Origin'] = 'http://0.0.0.0:8000'
  if params[:image] && params[:image][:filename]
    filename = params[:image][:filename]
    file = params[:image][:tempfile]
    path = "./upload/#{filename}"
    Dir.mkdir(UPLOAD_DIR_NAME) unless Dir.exist?(UPLOAD_DIR_NAME)
    File.open(path, 'wb') do |f|
      f.write(file.read)
    end
  end
  200
end
