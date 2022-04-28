from flask import render_template, request, redirect, url_for, flash
from crud import app, db
from crud.models import InductionTraining, Planning, OtherTraining


@app.route('/')
def index():
    return render_template("header.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404


@app.route('/info')
def info():
    return render_template("info.html")


@app.route('/accounting')
def accounting():
    return render_template("journals.html")


@app.route('/induction_training')
def induction_training():
    all_data = InductionTraining.query.all()
    return render_template("induction_training.html", employees=all_data)


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


@app.route('/deleteAcc/<id_obj>/', methods=['GET', 'POST'])
def delete_accounting(id_obj):
    my_data = InductionTraining.query.get(id_obj)
    db.session.delete(my_data)
    db.session.commit()
    flash("Объект успешно удалён")

    return redirect(url_for('induction_training'))


"""Остальные инструктажи"""


@app.route('/other_training')
def other_training():
    all_data = OtherTraining.query.all()
    return render_template("other_training.html", employees=all_data)


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


@app.route('/deleteAccOth/<id_obj>/', methods=['GET', 'POST'])
def delete_accounting_oth(id_obj):
    my_data = OtherTraining.query.get(id_obj)
    db.session.delete(my_data)
    db.session.commit()
    flash("Объект успешно удалён")

    return redirect(url_for('other_training'))


"""Для планирования"""


@app.route('/planning')
def planning():
    all_data = Planning.query.all()
    return render_template("planning.html", employees=all_data)


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


@app.route('/deletePl/<id_obj>/', methods=['GET', 'POST'])
def delete_planning(id_obj):
    my_data = Planning.query.get(id_obj)
    db.session.delete(my_data)
    db.session.commit()
    flash("Объект успешно удален")
    return redirect(url_for('planning'))
