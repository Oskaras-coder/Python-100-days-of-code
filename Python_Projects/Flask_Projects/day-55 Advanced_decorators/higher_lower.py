from flask import Flask
import random

app = Flask(__name__)
random_number = random.choice(range(0, 10))
print(random_number)

@app.route("/")
def guess_number():
    return "<h1>Guess a number between 0 and 9<h1/>" \
           "<img src='https://media3.giphy.com/media/fDUOY00YvlhvtvJIVm/200w.webp?cid" \
           "=ecf05e47lkho3k4tbxk3c3wj6xgf60untesev6zfu8bwxvli&ep=v1_gifs_search&rid=200w.webp&ct=g' width=500>"


@app.route("/<int:number>")
def check_higher_lower(number):
    if random_number > number:
        return "<h1 style='color: red'>Too low, try again!<h1/>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif random_number < number:
        return "<h1 style='color: red'>Too high, try again<h1/>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return f"<h1 style='color: green'>Congrats!! The number was {number}! <h1/>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
