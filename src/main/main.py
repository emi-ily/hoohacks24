from flask import Flask, render_template, request
import os
from propelauth_flask import TokenVerificationMetadata, init_auth, current_user


app = Flask(__name__)


# You can find your Verifier Key under Backend Integration in the dashboard.
#   This skips a network request to fetch the key on startup.
auth = init_auth(
    "https://59223397842.propelauthtest.com",
    "608b45fdc719549f347b990b408a1159f800ad283d94dab0c11b60e4525114492ede59d57ff7ea8965f493f1f9965687",
    TokenVerificationMetadata(
        verifier_key="""
            -----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxEr1NiOPUwWAFvshMUX2
tVC4h75tHbo9e9YD/wjX2IEUykmInCzsioUyeEUn1BFkMHTicnB3npa8OxQJRrmx
/JSki1NXv3dlhlkE+M/SegmU91qZsJXCsAoKmlvsoBAFFz30OUr5vPfGrHQRkgkr
00e6q2BqL7GYeRr7smEOHlf+XoYU2S17m7UcIL9o3bkchz/TNtxIkrbmb+fasSwQ
0guC8PDn3ojPmK3V5jxNQsLAJgkMAZGu/g+4ru7mE3JBjaheEDhPsH5jyHGErJaJ
Ao50HS/ADPBPKg2bc57HCwdv99YhALUM8sL609p9JB83RJgJaaJ9SNTcNiUsIGwt
bwIDAQAB
-----END PUBLIC KEY-----
        """,
        issuer="https://59223397842.propelauthtest.com",
    ),
)


@app.route("/loggedin", methods=['GET','POST'])
def get_user():
    email = request.form["email"]
    user = auth.fetch_user_metadata_by_email(
        email,
        include_orgs=False,
    )
    return render_template("index.html", user=user.get("user_id"))

@app.route("/api/whoami")
@auth.optional_user
def who_am_i_optional():
    if current_user.exists():
        return {"user_id": current_user.user_id}
    return {}


@app.route("/")
def home():
    return render_template("index.html", user="idk this user...")


@app.route("/navigation")
def links():
    return render_template("links.html")

@app.route("/random")
def random():
    return render_template("random.html")


if __name__ == "__main__":
    app.run()
