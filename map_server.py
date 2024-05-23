from bottle import route, run, get, post,request,static_file
import json,random

from gevent import monkey; monkey.patch_all()



@route('/hello')
def hello():
    return "Hello World!"

# @route('/')
# def main():
#     return static_file('main.html', root='static/')

@get('/map')
def get_map():
    return random.choice(existed_data)

@get('/list')
def map_list():
    return "<br>".join(existed_data)

# @get('/add_exception')
# def add_exception():
#     return static_file('add_exception.html', root='static/')

@post('/add_map')
def add_exception_backend():
    print(request.json)
    data = request.json
    text=data['text']
    if text not in existed_data:
        existed_data.append(text)
        with open("maps.json",'w', encoding='utf-8') as f:
            json.dump(existed_data, f, ensure_ascii=False, indent=4)
        return {"status": "success"}
    else:
        return {"status": "already exists"}


with open("maps.json", encoding='utf-8') as f:
    existed_data=json.load(f)
    # print(existed_data)

with open("config.json", encoding='utf-8') as f:
    config=json.load(f)

run(host=config['host'], port=config['port'], debug=config['debug'],server='gevent')