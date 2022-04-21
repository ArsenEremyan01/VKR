from flask import render_template, request, redirect, url_for, flash

from crud import app, db
from crud.models import Accounting, Planning


@app.route('/')
def index():
    return render_template("header.html")


@app.route('/info')
def info():
    return render_template("info.html")


@app.route('/accounting')
def accounting():
    all_data = Accounting.query.all()

    return render_template("accounting.html", employees=all_data)


@app.route('/insertAcc', methods=['POST'])
def insert_accounting():
    if request.method == 'POST':
        fio = request.form['fio']
        udos = request.form['udos']
        podrz = request.form['podrz']
        workpl = request.form['workpl']
        dolj = request.form['dolj']
        status = request.form['status']
        date_pas = request.form['date_pas']

        # srok = request.form['srok']

        my_data = Accounting(fio, udos, podrz, workpl, dolj, status, date_pas)

        db.session.add(my_data)
        db.session.commit()

        flash("Объект успешно добавлен")

        return redirect(url_for('accounting'))


# this is our update route where we are going to update our employee
@app.route('/updateAcc', methods=['GET', 'POST'])
def update_accounting():
    if request.method == 'POST':
        my_data = Accounting.query.get(request.form.get('id'))
        my_data.fio = request.form['fio']
        my_data.udos = request.form['udos']
        my_data.podrz = request.form['podrz']
        my_data.workpl = request.form['workpl']
        my_data.dolj = request.form['dolj']
        my_data.status = request.form['status']
        my_data.date_pas = request.form['date_pas']

        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('accounting'))


# This route is for deleting our employee
@app.route('/deleteAcc/<id_obj>/', methods=['GET', 'POST'])
def delete_accounting(id_obj):
    my_data = Accounting.query.get(id_obj)
    db.session.delete(my_data)
    db.session.commit()
    flash("Объект успешно удален")

    return redirect(url_for('accounting'))


"""Для планирования"""


@app.route('/planning')
def planning():
    all_data = Planning.query.all()

    return render_template("planning.html", employees=all_data)


@app.route('/insertPl', methods=['POST'])
def insert_planning():
    if request.method == 'POST':
        podrz_plan = request.form['podrz_plan']
        goal = request.form['goal']
        work_plan = request.form['work_plan']
        date_plan = request.form['date_plan']
        my_data = Planning(podrz_plan, goal, work_plan, date_plan)

        db.session.add(my_data)
        db.session.commit()

        flash("Объект успешно добавлен")

        return redirect(url_for('planning'))


# this is our update route where we are going to update our employee
@app.route('/updatePl', methods=['GET', 'POST'])
def update_planning():
    if request.method == 'POST':
        my_data = Planning.query.get(request.form.get('id'))
        my_data.podrz_plan = request.form['podrz_plan']
        my_data.goal = request.form['goal']
        my_data.work_plan = request.form['work_plan']
        my_data.date_plan = request.form['date_plan']
        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('planning'))


@app.route('/deletePl/<id_obj>/', methods=['GET', 'POST'])
def delete_planning(id_obj):
    my_data = Planning.query.get(id_obj)
    db.session.delete(my_data)
    db.session.commit()
    flash("Объект успешно удален")
    return redirect(url_for('planning'))

# TODO сделать даты
# TODO Вход на сайт по ключу
# TODO если авторизован то роут не на "вход", а на другую страницу
# TODO logging

# TODO создать таблицу для
# TODO
# TODO


# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <link rel="stylesheet" href="static/css/style.css">
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
# <header>
#     <div class="active">
#         <nav>
#             <a href="{{ url_for('index') }}" class="logo"><img src="static/img/header1.png"
#                                                                width="85" height="35"></a>
#             <a href="{{ url_for('accounting') }}">Учёт</a>
#             <a href="{{ url_for('planning') }}">Планирование</a>
#             <a href="{{ url_for('info') }}">Информация</a>
#         </nav>
#
#     </div>
# </header>
# </body>
# </html>