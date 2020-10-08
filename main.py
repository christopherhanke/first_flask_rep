from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    current_year = datetime.datetime.now().year
    some_text = "Message from the handler"

    cities = ["Boston", "Vienna", "Paris", "Berlin"]

    return render_template(
        "index.html",
        current_year=current_year,
        some_text=some_text,
        cities=cities
    )


@app.route("/about")
def about_me():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


if __name__ == "__main__":
    app.run(debug=True)
