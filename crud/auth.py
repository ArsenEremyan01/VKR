from crud.models import *
from flask import render_template, redirect, url_for, request, flash, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        name = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=name).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.open_main_page'))
            else:
                flash('Неверный пароль.', category='error')
        else:
            flash('Почты не существует.', category='error')

    return render_template('login.html', user=current_user)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=name).first()
        if user:
            flash('Эл. адрес уже существует.', category='error')
        elif len(name) < 4:
            flash('Электронная почта должна быть больше 3 символов.', category='error')
        elif password != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password) < 7:
            flash('Пароль должен быть не менее 7 символов.', category='error')
        else:
            new_user = User(email=name, password=generate_password_hash(password2, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Аккаунт создан!', category='success')
            return redirect(url_for('auth.login'))
    return render_template('register.html', user=current_user)


@login_required
@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('views.open_first_page'))
