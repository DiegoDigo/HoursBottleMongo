import os
from bottle import Bottle, response
from bson.json_util import dumps, loads
from models import User

app = Bottle()


@app.get('/')
def index():
    response.content_type = 'application/json'
    user = User.objects(username="diego")
    return dumps(loads(user.to_json()))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='127.0.0.1', port=port, debug=True, reloader=True)
