import os
from bottle import Bottle

app = Bottle()


@app.get('/')
def index():
    return "<h1>Funcionando</h1>"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='127.0.0.1', port=port, debug=True, reloader=True)