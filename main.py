from flask import Flask
from rest.routes import app as app_words

app = Flask(__name__)

apps = (app_words,)
for _app in apps:
    app.register_blueprint(_app)

if __name__ == '__main__':
    app.run(port=8080)
