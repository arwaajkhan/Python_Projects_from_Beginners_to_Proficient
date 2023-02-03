from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"

    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Helo, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/O58wTsoBqBqMw/giphy.gif" width=300>'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"


@app.route('/user/<path:username>/<int:number>')
def greeting(username, number):
    return f"Hello there {username}, you are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)
