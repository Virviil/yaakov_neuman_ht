import flask

from rest import controller

app = flask.Blueprint('words', __name__, url_prefix='/words')


@app.route('', methods=['POST'])
def set_words():
    js = flask.request.json
    return controller.set_words(js)


@app.route('')
def get_words_stat():
    return controller.get_words_stat()
