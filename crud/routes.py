from crud import app
from crud.models import *
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash


@app.route('/', methods=['GET'])
def open_first_page():
    return render_template("first_page.html")


@login_required
@app.route('/info')
def info():
    return render_template("info.html")


@login_required
@app.route('/main_content', methods=['GET'])
def open_main_page():
    return render_template('main_content.html')


@login_required
@app.route('/accounting')
def accounting():
    return render_template("journals.html")


"""авторизация"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    name = request.form.get('email')
    password = request.form.get('password')

    if name and password:
        user = User.query.filter_by(email=name).first()

        if user and check_password_hash(user.password, password):
            rm = True if request.form.get('remainme') else False
            login_user(user, remember=rm)
            return redirect(url_for('open_main_page'))
        else:
            flash('Неверный логин или пароль')
    else:
        flash('Пожалуйста, заполните все поля')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    name = request.form.get('email')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    if request.method == 'POST':
        if not (name or password or password2):
            flash('Пожалуйста, заполните все поля')
        if User.query.filter_by(email=name).first():
            flash('Данный пользователь зарегистрирован')
        elif len(password) < 8:
            flash('Минимальная длина пароля: 8 ')
        elif password != password2:
            flash('Пароли не совпадают')
        new_user = User(email=name, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@login_required
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('open_first_page'))


"""Вводный инструктаж"""


@login_required
@app.route('/induction_training')
def induction_training():
    all_data = InductionTraining.query.all()
    return render_template("induction_training.html", employees=all_data)


@login_required
@app.route('/insertAcc', methods=['POST'])
def insert_accounting():
    if request.method == 'POST':
        briefing_date = request.form['briefing_date']
        employee_name = request.form['employee_name']
        birthdate = request.form['birthdate']
        position = request.form['position']
        subdivision = request.form['subdivision']
        instructor_name = request.form['instructor_name']

        my_data = InductionTraining(briefing_date, employee_name, birthdate, position, subdivision, instructor_name)

        db.session.add(my_data)
        db.session.commit()

        flash("Объект успешно добавлен")

        return redirect(url_for('induction_training'))


@login_required
@app.route('/updateAcc', methods=['GET', 'POST'])
def update_accounting():
    if request.method == 'POST':
        my_data = InductionTraining.query.get(request.form.get('id'))
        my_data.briefing_date = request.form['briefing_date']
        my_data.employee_name = request.form['employee_name']
        my_data.birthdate = request.form['birthdate']
        my_data.position = request.form['position']
        my_data.subdivision = request.form['subdivision']
        my_data.instructor_name = request.form['instructor_name']

        db.session.commit()
        flash("Объект успешно обновлён")

        return redirect(url_for('induction_training'))


@login_required
@app.route('/deleteAcc/<id_obj>/', methods=['GET', 'POST'])
def delete_accounting(id_obj):
    my_data = InductionTraining.query.get(id_obj)
    db.session.delete(my_data)
    db.session.commit()
    flash("Объект успешно удалён")

    return redirect(url_for('induction_training'))


"""Остальные инструктажи"""


@login_required
@app.route('/other_training')
def other_training():
    all_data = OtherTraining.query.all()
    return render_template("other_training.html", employees=all_data)


@login_required
@app.route('/insertAccOth', methods=['POST'])
def insert_accounting_oth():
    if request.method == 'POST':
        briefing_date = request.form['briefing_date']
        employee_name = request.form['employee_name']
        birthdate = request.form['birthdate']
        position = request.form['position']
        type_of_briefing = request.form['type_of_briefing']
        instructor_name = request.form['instructor_name']
        next_briefing = request.form['next_briefing']

        my_data = OtherTraining(briefing_date, employee_name, birthdate,
                                position, type_of_briefing, instructor_name, next_briefing)

        db.session.add(my_data)
        db.session.commit()

        flash("Объект успешно добавлен")

        return redirect(url_for('other_training'))


@login_required
@app.route('/updateAccOth', methods=['GET', 'POST'])
def update_accounting_oth():
    if request.method == 'POST':
        my_data = OtherTraining.query.get(request.form.get('id'))
        my_data.briefing_date = request.form['briefing_date']
        my_data.employee_name = request.form['employee_name']
        my_data.birthdate = request.form['birthdate']
        my_data.position = request.form['position']
        my_data.type_of_briefing = request.form['type_of_briefing']
        my_data.instructor_name = request.form['instructor_name']
        my_data.next_briefing = request.form['next_briefing']

        db.session.commit()
        flash("Объект успешно обновлён")

        return redirect(url_for('other_training'))


@login_required
@app.route('/deleteAccOth/<id_obj>/', methods=['GET', 'POST'])
def delete_accounting_oth(id_obj):
    my_data = OtherTraining.query.get(id_obj)
    db.session.delete(my_data)
    db.session.commit()
    flash("Объект успешно удалён")

    return redirect(url_for('other_training'))


"""Для планирования"""


@login_required
@app.route('/planning')
def planning():
    all_data = Planning.query.all()
    return render_template("planning.html", employees=all_data)


@login_required
@app.route('/insertPl', methods=['POST'])
def insert_planning():
    if request.method == 'POST':
        employee_name = request.form['employee_name']
        position = request.form['position']
        type_of_briefing = request.form['type_of_briefing']
        instructor_name = request.form['instructor_name']
        briefing_date = request.form['briefing_date']
        my_data = Planning(employee_name, position, type_of_briefing, instructor_name, briefing_date)

        db.session.add(my_data)
        db.session.commit()

        flash("Объект успешно добавлен")

        return redirect(url_for('planning'))


@login_required
@app.route('/updatePl', methods=['GET', 'POST'])
def update_planning():
    if request.method == 'POST':
        my_data = Planning.query.get(request.form.get('id'))
        my_data.employee_name = request.form['employee_name']
        my_data.position = request.form['position']
        my_data.type_of_briefing = request.form['type_of_briefing']
        my_data.instructor_name = request.form['instructor_name']
        my_data.briefing_date = request.form['briefing_date']
        db.session.commit()
        flash("Объект успешно обновлён")

        return redirect(url_for('planning'))


@login_required
@app.route('/deletePl/<id_obj>/', methods=['GET', 'POST'])
def delete_planning(id_obj):
    my_data = Planning.query.get(id_obj)
    db.session.delete(my_data)
    db.session.commit()
    flash("Объект успешно удален")
    return redirect(url_for('planning'))

#
# {% extends 'base.html' %}
# {% include 'scrollUp.html' %}
# {% block title %} Home {% endblock %}
# {% block body %}
#
# <div class="container">
#     <div class="row justify-content-center align-items-center">
#             <form class="form" method="POST">
#                 <div class="col-xs-12">
#                     <div class="form-group">
#                         <input type="email" name="email" class="form-control" placeholder="Ваш E-mail"/>
#                     </div>
#                 </div>
#                 <div class="col-xs-12">
#                     <div class="form-group">
#                         <input type="password" name="password" class="form-control" placeholder="Ваш пароль"/>
#                     </div>
#                 </div>
#                 <div class="text-center col-xs-12">
#                     <input class="btn btn-primary" type="submit" value="Авторизоваться">
#                     <a class="btn btn-primary" href="{{ url_for('register') }}">Регистрация</a>
#                     <input type="checkbox" name="remainme">Остаться в системе
#                 </div>
#             </form>
#     </div>
# </div>
# {% endblock %}
