from flask import Flask, render_template, request
import os
from propelauth_flask import TokenVerificationMetadata, init_auth, current_user

from calculate import calculate_emissions
from ecoScore import get_product_info, search_product

app = Flask(__name__)


class DataStore():
    user = None
    pic = "/static/user_dark.png"


data = DataStore()

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


@app.route("/loggedin", methods=['GET', 'POST'])
def get_user():
    email = request.form["email"]
    user = auth.fetch_user_metadata_by_email(
        email,
        include_orgs=False,
    )
    if user is not None:
        data.user = user
        data.pic = user.get("picture_url")
        return render_template("index.html", pfp=data.pic)
    else:
        return render_template("login.html", error="visible")


@app.route("/api/whoami")
@auth.optional_user
def who_am_i_optional():
    if current_user.exists():
        return {"user_id": current_user.user_id}
    return {}


@app.route("/")
def home():
    return render_template("index.html", pfp=data.pic)


@app.route("/navigation")
def links():
    return render_template("links.html")


@app.route("/random")
def random():
    return render_template("random.html", pfp=data.pic)


@app.route("/login")
def login():
    return render_template("login.html", error="hidden")


@app.route("/account")
def account():
    if data.user is None:
        no_user_vis = "visible"
        yes_user_vis = "hidden"
        username = " "
        my_name = None
    else:
        username = data.user.get("username")
        my_name = data.user.get("first_name")
        no_user_vis = "hidden"
        yes_user_vis = "visible"
    return render_template("account.html", no_user=no_user_vis, yes_user=yes_user_vis, user=username, name=my_name,
                           error="hidden")


@app.route('/search', methods=['POST'])
def search():
    product_name = request.form['product_name']
    if product_name == "":
        return render_template("foodsearch.html", error="visible", item="[no name]")
    product_count = search_product(product_name)
    if product_count == 0:
        return render_template("foodsearch.html", error="visible", item=product_name)
    product_info = get_product_info(product_name)

    return render_template('result.html', product_info=product_info, product_name=product_name, pfp=data.pic)


@app.route('/foodsearch')
def food_find():
    return render_template('foodsearch.html', error="hidden", item="", pfp=data.pic)

@app.route('/footprintcalculation')
def footprint_find():
    return render_template('footprint.html', error="hidden", item="", pfp=data.pic)

@app.route('/aboutme')
def about_me():
    return render_template('aboutme.html', error="hidden", item="")


@app.route('/calculate', methods=['POST'])
def calculate():
    food = request.form['food']
    servings = float(request.form['servings'])
    emissions = calculate_emissions(food, servings)
    return render_template('calculationresult.html', food=food, servings=servings, emissions=emissions, pfp=data.pic)


if __name__ == "__main__":
    app.run()
