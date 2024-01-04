from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapped_function():
        return "<b>" + function() + "</b>"

    return wrapped_function


def make_emphasis(function):
    def wrapped_function():
        return "<em>" + function() + "</em>"

    return wrapped_function


def make_underlined(function):
    def wrapped_function():
        return "<u>" + function() + "</u>"

    return wrapped_function


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, Hanna!</h1>" \
           "<p>New paragraph<p>" \
           "<img src=https://www.lomsnesvet.ca/wp-content/uploads/sites/21/2019/08/Kitten-Blog-683x1024.jpg " \
           "alt='kitten' width=200>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"


if __name__ == "__main__":
    app.run(debug=True)
