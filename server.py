from flask import Flask, render_template, request, session, redirect


app = Flask(__name__)


@app.route("/")
def home():
    """Homepage where users login"""

    return render_template("home.html")


if __name__ = "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
