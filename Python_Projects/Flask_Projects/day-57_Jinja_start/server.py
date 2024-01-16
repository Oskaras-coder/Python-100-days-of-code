from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year_number = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=year_number)


@app.route("/guess/<string:name>")
def check_the_name(name):
    json_url_gender = f"https://api.genderize.io/?name={name}"
    gender_json_file = requests.get(url=json_url_gender).json()
    gender = gender_json_file["gender"]

    json_url_age = f"https://api.agify.io?name={name}"
    age_json_file = requests.get(url=json_url_age).json()
    age = age_json_file["age"]

    return render_template("guess.html", name=name.capitalize(), gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_data = requests.get(blog_url).json()
    return render_template("blog.html", posts=blog_data)

if __name__ == "__main__":
    app.run(port=5001,
            debug=True)
