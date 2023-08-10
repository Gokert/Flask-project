from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField


class VacancyAddForm(FlaskForm):
    head = StringField('Position')
    text = TextAreaField('Text')
    salary = IntegerField('Salary')
    submit = SubmitField("Enter")
