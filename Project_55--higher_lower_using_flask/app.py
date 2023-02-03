from flask import Flask
import random

app = Flask(__name__)
ran_num = random.randint(0, 9)


@app.route('/')
def hello():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def rand_number(number):
    if number < ran_num:
        return '<h1 style="color: red">Too Low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/SeSZsBrPAQqi72mkwN/giphy.gif">'
    elif number > ran_num:
        return '<h1 style="color: purple">Too High, try again!</h1>' \
               '<img src="https://media.giphy.com/media/8HInngFE5fDI43kra5/giphy-downsized-large.gif">'
    else:
        return '<h1 style="color: green">You Found me</h1>' \
               '<img src="https://media.giphy.com/media/VP00pDms5LTHuOmER3/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
