from flask import Flask, render_template, g, redirect, url_for, request
from flask_oidc import OpenIDConnect
from okta import UsersClient
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

import send_email


app = Flask(__name__)
app.config["OIDC_CLIENT_SECRETS"] = "client_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
app.config["SECRET_KEY"] = "zDEKy7o72BpHP6HoKKdpn9phZ0GLBCXOrlsdHfMz"
app.config["OIDC_ID_TOKEN_COOKIE_NAME"] = "oidc_token"
oidc = OpenIDConnect(app)
okta_client = UsersClient("dev-77597864.okta.com", "00kZYOp_8Mwx-1JOmgUku77h8JzMplmQ7n-clS7Rzn")


@app.before_request
def before_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
    else:
        g.user = None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname = request.form['uname']
        email = request.form['email']
        fname = request.form['fname']
        lname = request.form['lname']
        studies = request.form['studies']
        center = request.form['center']
        interest = request.form['interest']
    return render_template("signup.html")


@app.route("/dashboard")
# @oidc.require_login
def dashboard():
    return render_template("dashboard.html")


@app.route("/login")
# @oidc.require_login
def login():
    return redirect(url_for(".dashboard"))


@app.route("/logout")
def logout():
    # oidc.logout()
    return redirect(url_for(".index"))