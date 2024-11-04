from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, request, flash, redirect, url_for


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if not user:
            flash('Username does not exist.', category='error')
        else:
            if not check_password_hash(user.password, password):
                flash('Incorrect password, try again.', category='error')
            else:
                flash('Login successfully!', category='success')
                return redirect(url_for('views.home'))

    return render_template('login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        if User.query.filter_by(username=username).first():
            flash('Username has already existed.', category='error')
        elif User.query.filter_by(email=email).first():
            flash('Email has already existed.', category='error')
        elif len(email) < 3:
            flash('Email is invalid.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character.', category='error')
        elif len(password) < 3:
            flash('Password must be at least 3 characters.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth.route('/loading')
def loading():
    return render_template('loading.html')
