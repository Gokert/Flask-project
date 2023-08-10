from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField


class EditInterviewForm(FlaskForm):
    choices = ['no', 'yes']
    choices_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = SelectField("Result", choices=choices)
    scores = SelectField("Scores", choices=choices_int)
    name_emp = StringField("Name_emp")
    int_date = DateField("Date of the event")
    submit = SubmitField("Enter")
