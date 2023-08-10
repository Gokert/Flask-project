from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, TextAreaField


class VacancyUserForm(FlaskForm):
    choices = ["male", "female"]

    name = StringField("Name")
    address = StringField("Address")
    gender = SelectField("Gender", choices=choices)
    education = StringField("Education")
    birthday = DateField("Birthday")
    resume = TextAreaField("Resume")

    submit = SubmitField("Enter")
