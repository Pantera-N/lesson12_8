from flask import Flask

app = Flask(__name__)


@app.route('/users/<uid>')
def profile(uid):
   print(uid)
   print(type(uid))

   return ""
