from crud.models import *
from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def open_first_page():
    return render_template("first_page.html")


@login_required
@views.route('/info')
def info():
    data = current_user.email
    return render_template("info.html", data=data)


@login_required
@views.route('/main_content', methods=['GET'])
def open_main_page():
    return render_template('main_content.html')


@login_required
@views.route('/accounting')
def accounting():
    return render_template("journals.html")


"""Вводный инструктаж"""


@login_required
@views.route('/induction_training')
def induction_training():
    all_data = InductionTraining.query.filter_by(user_id=current_user.id).all()
    return render_template("induction_training.html", employees=all_data)


@login_required
@views.route('/insertAcc', methods=['POST'])
def insert_accounting():
    if request.method == 'POST':
        briefing_date = request.form['briefing_date']
        employee_name = request.form['employee_name']
        birthdate = request.form['birthdate']
        position = request.form['position']
        subdivision = request.form['subdivision']
        instructor_name = request.form['instructor_name']

        my_data = InductionTraining(briefing_date, employee_name, birthdate, position,
                                    subdivision, instructor_name, current_user.id)

        db.session.add(my_data)
        db.session.commit()

        flash("Объект успешно добавлен")

        return redirect(url_for('views.induction_training'))


@login_required
@views.route('/updateAcc', methods=['GET', 'POST'])
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

        return redirect(url_for('views.induction_training'))


@login_required
@views.route('/deleteAcc/<id_obj>/', methods=['GET', 'POST'])
def delete_accounting(id_obj):
    my_data = InductionTraining.query.get(id_obj)
    db.session.delete(my_data)
    db.session.commit()
    flash("Объект успешно удалён")

    return redirect(url_for('views.induction_training'))


"""Остальные инструктажи"""


@login_required
@views.route('/other_training')
def other_training():
    all_data = OtherTraining.query.filter_by(user_id=current_user.id).all()
    return render_template("other_training.html", employees=all_data)


@login_required
@views.route('/insertAccOth', methods=['POST'])
def insert_accounting_oth():
    if request.method == 'POST':
        briefing_date = request.form['briefing_date']
        employee_name = request.form['employee_name']
        birthdate = request.form['birthdate']
        position = request.form['position']
        type_of_briefing = request.form['type_of_briefing']
        instructor_name = request.form['instructor_name']
        next_briefing = request.form['next_briefing']

        my_data = OtherTraining(briefing_date, employee_name, birthdate, position,
                                type_of_briefing, instructor_name, next_briefing, current_user.id)

        db.session.add(my_data)
        db.session.commit()

        flash("Объект успешно добавлен")

        return redirect(url_for('views.other_training'))


@login_required
@views.route('/updateAccOth', methods=['GET', 'POST'])
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

        return redirect(url_for('views.other_training'))


@login_required
@views.route('/deleteAccOth/<id_obj>/', methods=['GET', 'POST'])
def delete_accounting_oth(id_obj):
    my_data = OtherTraining.query.get(id_obj)
    db.session.delete(my_data)
    db.session.commit()
    flash("Объект успешно удалён")

    return redirect(url_for('views.other_training'))


"""Для планирования"""


@login_required
@views.route('/planning')
def planning():
    all_data = Planning.query.filter_by(user_id=current_user.id).all()
    return render_template("planning.html", employees=all_data)


@login_required
@views.route('/insertPl', methods=['POST'])
def insert_planning():
    if request.method == 'POST':
        employee_name = request.form['employee_name']
        position = request.form['position']
        type_of_briefing = request.form['type_of_briefing']
        instructor_name = request.form['instructor_name']
        briefing_date = request.form['briefing_date']
        my_data = Planning(employee_name, position, type_of_briefing,
                           instructor_name, briefing_date, current_user.id)

        db.session.add(my_data)
        db.session.commit()

        flash("Объект успешно добавлен")

        return redirect(url_for('views.planning'))


@login_required
@views.route('/updatePl', methods=['GET', 'POST'])
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

        return redirect(url_for('views.planning'))


@login_required
@views.route('/deletePl/<id_obj>/', methods=['GET', 'POST'])
def delete_planning(id_obj):
    my_data = Planning.query.get(id_obj)
    db.session.delete(my_data)
    db.session.commit()
    flash("Объект успешно удален")
    return redirect(url_for('views.planning'))
