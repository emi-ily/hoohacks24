from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/navigation")
def links():
    return render_template("links.html")


if __name__ == "__main__":
    app.run()
