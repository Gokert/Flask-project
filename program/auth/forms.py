from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    login = StringField("Login", validators=[DataRequired(), Length(min=1, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField("Enter")
