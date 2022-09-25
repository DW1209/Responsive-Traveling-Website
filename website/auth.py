from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        if len(email) < 3:
            flash('Email is invalid.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character.', category='error')
        elif len(password) < 3:
            flash('Password must be at least 3 characters.', category='error')
        else:
            flash('Account created!', category='success')

    return render_template('register.html')

@auth.route('/loading')
def loading():
    return render_template('loading.html')