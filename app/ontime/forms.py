# AIKATAULUNÄKYMIEN LOMAKKEET

from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
import app.ontime.wrangle as wr


# PYSÄKKIKOHTAINEN VIIVE
class OnTimeStopForm(FlaskForm):

    pysakki = SelectField("Pysäkki: ", choices=wr.get_stops_tuple())
    submit = SubmitField("Näytä")
