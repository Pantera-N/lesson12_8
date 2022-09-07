from flask import Flask

app = Flask(__name__)


@app.route('/users/<uid>')
def profile(uid):
    return f'<h1>Профиль {uid}</h1>'


@app.route('/catalog/items/<itemid>')
def profile(itemid):
    return f'<h1>Страничка товара {itemid}</h1>

