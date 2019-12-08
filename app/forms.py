from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, Length, InputRequired

# KIRJAUTUMISSIVUN LOMAKE

class LoginForm(FlaskForm):

    email = StringField("Sähköpostiosoite: ", validators=[InputRequired(), Email(message="Virheellinen osoite"), Length(max=64)])
    password = PasswordField("Salasana: ", validators=[InputRequired(), Length(min=6, max=20)])
