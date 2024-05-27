from bottle import route, run, get, post,request,static_file,Response,response
import json,random

from gevent import monkey; monkey.patch_all()



@route('/hello')
def hello():
    return "Hello World!"

@get('/game')
def main():
    return static_file('start.htm',root='')

@get('/lib/<filename>')
def libs(filename):
    return static_file(filename,root='lib/')

@get('/resources/<filename>')
def resources(filename):
    return static_file(filename,root='resources/')

@get('/map')
def get_map():
    # resp=Response(body=random.choice(existed_data))
    response.add_header("Access-Control-Allow-Origin","*")
    response.content_type="application/json"
    #response.add_header("test", True)
    return random.choice(existed_data)


@get('/list')
def map_list():
    return "<br>".join(existed_data)

# @get('/add_exception')
# def add_exception():
#     return static_file('add_exception.html', root='static/')

@post('/add_map')
def add_map_api():
    print(dir(request.body))
    # data = request.body.read().decode('utf-8')
    data = request.json()
    if data not in existed_data:
        existed_data.append(data)
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
# run(host=config['host'], port=config['port'], debug=config['debug'])
