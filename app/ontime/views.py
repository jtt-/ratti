# AIKATAULUDATAAN LIITTYVÄT NÄKYMÄT

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from app import db

from app.ontime.forms import OnTimeStopForm
import app.ontime.graph as graphs

# Tähän tiedostoon ohjaava blueprint
ontime_blueprint = Blueprint("ontime", __name__, template_folder="templates/ontime")

# PYSÄKKIKOHTAINEN VIIVE

@ontime_blueprint.route('/ontime_stop', methods=["GET", "POST"])
@login_required
def ontime_stop():

    form = OnTimeStopForm()
    #tulokset = testi.query.get()
    if form.validate_on_submit():
        pysakki = form.pysakki.data
        graph = graphs.ontime_stop_graph(pysakki)
        return render_template("ontime_stop.html", form=form, graph=graph)

    return render_template("ontime_stop.html", form=form, graph="Valitse pysäkki")

# REITIN SEURANTA

@ontime_blueprint.route('/ontime_route', methods=["GET", "POST"])
@login_required
def ontime_route():

    return render_template("ontime_route.html")
