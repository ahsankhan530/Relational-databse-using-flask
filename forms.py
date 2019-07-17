from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from projet.models import User

class RegistrationForm(FlaskForm):
    nom = StringField('Nom',
                           validators=[DataRequired(), Length(min=2, max=20)])

    prenom = StringField('Prénom',
                           validators=[DataRequired(), Length(min=2, max=20)])

    adresse = StringField('adresse postale',
                           validators=[DataRequired(), Length(min=2, max=100)])    

    id = StringField('N° vital',
                            validators=[DataRequired(), Length(13)])

    mail = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('mot de passe', validators=[DataRequired()])

    confirm_password = PasswordField('resaisir le mot de passe',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("s'inscrire")

    def check_cartevitale(self, id):
        user = User.query.filter_by(id=id.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def check_mail(self, mail):
        user = User.query.filter_by(mail=mail.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    mail = StringField('Mail',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    remember = BooleanField('Se souvenir')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    mail = StringField('Email',
                        validators=[DataRequired(), Email()])

    submit = SubmitField("modifier")

    def check_mail(self, mail):
        if mail.data != current_user.mail :
            user = User.query.filter_by(mail=mail.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')



