# DEMAND VIEWS - NOUSUTIETOIHIN LIITTYVÄT NÄKYMÄT

from flask import Blueprint, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from app import db # __init__.py määritelty tietokanta
#from app.models import model # ei tarvita kuin sqlalchemyn kanssa
from app.demand.forms import DemandForm, EventsByLine
import app.demand.wrangle as wr
import app.demand.graph as gr

demand_blueprint = Blueprint("demand", __name__, template_folder="templates/demand")

# LINJAN KÄYTTÖASTE

@demand_blueprint.route("/line_usage", methods = ["GET", "POST"])
@login_required
def line_usage():
    form = DemandForm()

    if form.validate_on_submit:
        linja = form.linja.data
        usage = wr.get_events(linja)
        return render_template("line_usage.html", form = form, usage = usage)

    return render_template("line_usage.html", form = form, usage = "valitse linja")


# LINJAKOHTAISET TAPAHTUMAT

@demand_blueprint.route("/events_by_line", methods = ["GET", "POST"])
@login_required
def events_by_line():
    form = EventsByLine()

    if form.validate_on_submit():
        linja = form.linja.data
        alkupvm = form.alkupvm.data
        loppupvm = form.loppupvm.data

        graafi = gr.events_by_line_graph(linja, alkupvm, loppupvm)

        return render_template("events_by_line.html", form=form, graafi=graafi)

    return render_template("events_by_line.html", form=form, graafi=None)
