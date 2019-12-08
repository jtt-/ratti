from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.fields.html5 import DateField
import app.demand.wrangle as wr

# TESTAUKSEEN

class DemandForm(FlaskForm):

    linja = SelectField("Linja: ", choices=wr.get_lines_tuple())
    submit = SubmitField("OK")

# LINJAKOHTAISET TAPAHTUMAT

class EventsByLine(FlaskForm):

    linja = SelectField("Linja: ", choices=wr.get_lines_tuple())
    alkupvm = DateField("Alkupvm: ")
    loppupvm = DateField("Loppupvm: ")
    submit = SubmitField("OK")
