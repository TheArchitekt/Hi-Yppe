from flask import Flask, render_template, request, session, redirect


app = Flask(__name__)


@app.route("/")
def home():
    """Homepage where users login"""

    return
