from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, DateField, IntegerField
from wtforms.validators import DataRequired, Length


class EmployeeAddForm(FlaskForm):
    login = StringField("Login", validators=[DataRequired(), Length(min=1, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=1, max=20)])
    remember = BooleanField("Remember", default=False)

    name = StringField("Name", validators=[DataRequired(), Length(min=1, max=20)])
    birthday = DateField("Birthday")
    address = StringField("Address")
    education = StringField("Education")
    enroll_date = DateField("Enroll date")
    salary = IntegerField("Salary")
    position = StringField("Position")
    submit = SubmitField("Enter")
