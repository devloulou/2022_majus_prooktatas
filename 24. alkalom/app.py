"""
Flask - lightweight web framework a pythonhoz
webes backendet illetve rest api-kat

Django - heawyweight -

"""

from flask import Flask

app = Flask("valami")

@app.route("/")
def hello():
    return "Hello world/"


@app.route("/egyik")
def masik():
    return "Hello world masik/"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
