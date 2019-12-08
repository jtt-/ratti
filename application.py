from app import app, db
from app.models import *
from app.forms import LoginForm

from flask import render_template, redirect, request, url_for, flash, session, Flask
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


# SAAVUTTAESSA NÄYTETÄÄN index.html JOS SESSIO ON KIRJAUTUNUT

@app.route('/')
@login_required
def index():
    return render_template('index.html')

# FLASK_LOGIN OHJAA KIRJAUTUMISSIVULLE AINA KUN SESSIO EI OLE KIRJAUTUNUT

@app.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated == True:
        return redirect(url_for('index'))

    form = LoginForm()

    if request.method == 'POST' and form.validate():
        check_user = User.objects(email=form.email.data).first()

        if check_user:
            if check_password_hash(check_user['password'], form.password.data):
                login_user(check_user)
                return redirect(url_for("index"))

    return render_template("login.html", form=form)

# ULOSKIRJAAMINEN

@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# VIRHESIVUT
# 404

@app.errorhandler(404)
@login_required
def page_not_found(e):
    return render_template('error.html'), 404

# SOVELLUKSEN KÄYNNISTYS

if __name__ == "__main__":
    app.run(debug=True)
