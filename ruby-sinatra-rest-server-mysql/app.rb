require 'sinatra'
require 'json'

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

put '/users/upload' do
  request_header = ''
  upload_dir_name = 'upload'
  Dir.mkdir(upload_dir_name) unless Dir.exist?(upload_dir_name)
  body = request.body.read
  content_length = request.env['CONTENT_LENGTH'].to_i
  rack_request_form_hash = request.env['rack.request.form_hash']
  target_form_data = rack_request_form_hash['picture']
  target_form_data.map{|k,v|
    if 'head' == k.id2name
      request_header = v
    end
  }
  request_header_list = request_header.split(/\r\n/).map{|e|
    e.strip.split(/;/).map{|ee|
      ee.strip.split(/=|:/).each_slice(2).to_h
    }.flatten
  }.flatten
  save_file_fullname = ''
  content_type = ''
  request_header_list.map{|e|
    if e.keys[0].strip == 'filename'
      save_file_fullname = JSON.load(e.values[0].strip) # エスケープ対応
    end
    if e.keys[0].strip == 'Content-Type'
      content_type = e.values[0].strip
    end
  }
  save_file_name = save_file_fullname.split(/\./)[0]
  save_file_extension = 'png'

  save_file_path = File.join(upload_dir_name, save_file_name + '.' + save_file_extension)
  tmp = body.gsub(/[[:cntrl:]]\r\n/, 'うんこ').split(/\n/)
  start_end_index = tmp.map.with_index{|e, i| e == '' ? i : nil}.compact
  base64_str = tmp.slice((start_end_index[0] + 1)..(start_end_index[1] - 1)).join("\n")
  File.open('base64_str.txt', 'w') do |f|
    f.puts(base64_str)
  end
  File.open(save_file_path, 'wb') do |file|
    file.write(Base64.decode64(base64_str))
  end
  'ok'
end
