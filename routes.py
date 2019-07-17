from flask import Flask, render_template, url_for, flash, redirect, request
from projet.forms import RegistrationForm, LoginForm, UpdateAccountForm
from projet.models import User
from projet import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import os

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])

def register():
    if current_user.is_authenticated: 
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(nom=form.nom.data, prenom=form.prenom.data, adresse=form.adresse.data, id=1, mail=form.mail.data, password=password_hash)
        db.session.add(user)
        db.session.commit()
        flash(f'Le compte  {form.mail.data} a été bien crée !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(mail=form.mail.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('connexion refusé', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account", methods=['GET', 'POST'])
@login_required

def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.mail = form.mail.data
        db.session.commit()
        flash('votre compte a été mis à jour', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.mail.data = current_user.mail
    return render_template('account.html', title='Account', form=form)

@app.route('/upload')  
def upload():  
    return render_template("upload.html")  

@app.route('/add',methods=['POST'])
def add():
    print('aaaaaaaaaaaaa')
    file=request.files['inputFile']
    newfile= User(nam=file.filename,data=file.read(),)
    db.session.add(newfile)
    db.session.commit()
    return 'File upload sucessfully    '+ file.filename
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  

        return render_template("success.html")  