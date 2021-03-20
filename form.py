from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    fname = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    lname = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    submit = SubmitField('Registrar')
