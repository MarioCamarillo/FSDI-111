from flask import Flask

app = Flask(__name__)  # app is an instance


@app.route("/")
def index():
    return "<h1>Hello world!</h1>"


@app.route("/about")
def about():
    me = {
        "first_name": "Mario",
        "last_name" : "Camarillo",
        "hobbies"   : "programming microcontrollers",
        "active"    : True
    }
    return me
