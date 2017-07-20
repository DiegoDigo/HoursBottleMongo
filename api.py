import os
from bottle import Bottle, response
from bson.json_util import dumps, loads
from models import User

app = Bottle()


@app.get('/')
def index():
    try:
        user = User.objects()
        if user:
            response.status = 200
            response.content_type = 'application/json'
            return dumps(loads(user.to_json()))
        else:
            response.status = 404
            print("e vazia")
            response.content_type = 'application/json'
            return dumps(loads(user.to_json()))

    except ConnectionError as e:
        response.status = 500
        raise ConnectionError(e)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='127.0.0.1', port=port, debug=True, reloader=True)

