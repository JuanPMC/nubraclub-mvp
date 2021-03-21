from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

from send_email import send_email

app = Flask(__name__)

# CONFIG
app.config['SECRET_KEY'] = 'ClaveToSecretaAhiPalFormulario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# VIEW
Bootstrap(app)


# CONTROLLER
class SignupForm(FlaskForm):

    username = StringField('Usuario', validators=[DataRequired(), Length(max=25)])
    email = StringField('Email', validators=[DataRequired(), Email('Introduce un email valido')])
    fname = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    lname = StringField('Apellido', validators=[DataRequired(), Length(max=64)])
    studies = SelectField('Estudios', choices=[('preuni', 'Preuniversitario'),
                                               ('uni', 'Universitario')],
                          validators=[DataRequired()])
    grade = StringField('Curso actual', validators=[DataRequired(), Length(max=20)])
    center = StringField('Centro de estudios', validators=[DataRequired(), Length(max=50)])
    interest = StringField('Intereses', validators=[DataRequired(), Length(max=50)])
    aceparTerminosYemail = BooleanField("He leido y acepto los <a href=/static/politicaPrivacidad.pdf target=_blanck > terminos, condicioneas </a> y recibir emails con informacion sobre NibraClub.",validators=[DataRequired()])
    submit = SubmitField('Registrar')

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/droga")
def droga():
    return "Eres un jodido drogadicto, cabron deja de pensar en sustancias y ponte a currar!"

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            uname = request.form['username']
            email = request.form['email']
            fname = request.form['fname']
            lname = request.form['lname']
            studies = request.form['studies']
            grade = request.form['grade']
            center = request.form['center']
            interest = request.form['interest']

            message = """
            Subject: Nuevo usuario
            """ + 'username: ' + uname + '\nemail: ' + email + '\nfirstname: ' + fname + '\nlastname: ' + lname +\
                '\nstudies: ' + studies + '\ngrade: ' + grade + '\ncenter: ' + center + '\ninterest: ' + interest
            send_email(message)
            flash("Ya estas registrado!")
            return redirect(url_for('login'))
        else:
            flash("Error creating user!")
    return render_template('signup.html', form=form)


@app.route("/login")
def login():
    return render_template('login.html')
