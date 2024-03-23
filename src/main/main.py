from flask import Flask, render_template, request

from propelauth_flask import init_auth, current_user

auth = init_auth(
    "https://59223397842.propelauthtest.com",
    "608b45fdc719549f347b990b408a1159f800ad283d94dab0c11b60e4525114492ede59d57ff7ea8965f493f1f9965687",
)

app = Flask(__name__)


@app.route("/api/whoami")
@auth.require_user
def who_am_i():
    """This route is protected, current_user is always set"""
    return {"user_id": current_user.user_id}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/navigation")
def links():
    return render_template("links.html")


if __name__ == "__main__":
    app.run()
