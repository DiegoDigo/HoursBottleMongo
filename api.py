import os
from bottle import Bottle, response, request
from bson.json_util import dumps, loads
from models import User

app = Bottle()


@app.post('/')
def log():
    try:
        data = request.json
        if User.login(data["username"], data["password"]):
            response.status = 200
            response.content_type = 'application/json'
            return dumps(loads(User.buscar_usuario(data["username"]).to_json()))
        else:
            response.status = 404
            response.content_type = 'application/json'
            return "{}"
    except:
        response.status = 500
        raise ValueError("json invalido")


@app.get('/users')
def index():
    try:
        user = User.objects()
        if user:
            response.status = 200
            response.content_type = 'application/json'
            print(User.login("Diego", "261216"))
            return dumps(loads(user.to_json()))
        else:
            response.status = 404
            response.content_type = 'application/json'
            return dumps(loads(user.to_json()))

    except ConnectionError as e:
        response.status = 500
        raise ConnectionError(e)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='127.0.0.1', port=port, debug=True, reloader=True)