from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/angela")
def angela_cv():
    return render_template("angela_site.html")


if __name__ == "__main__":
    app.run(debug=True)
