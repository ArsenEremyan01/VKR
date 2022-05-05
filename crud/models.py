from datetime import datetime

from flask_login import UserMixin

from crud import db, manager


class InductionTraining(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    briefing_date = db.Column(db.String(15), nullable=False)
    employee_name = db.Column(db.String(80), nullable=False)
    birthdate = db.Column(db.String(15), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    subdivision = db.Column(db.String(50), nullable=False)
    instructor_name = db.Column(db.String(80), nullable=False)

    def __init__(self, briefing_date, employee_name, birthdate, position,
                 subdivision, instructor_name):
        self.briefing_date = briefing_date
        self.employee_name = employee_name
        self.birthdate = birthdate
        self.position = position
        self.subdivision = subdivision
        self.instructor_name = instructor_name


class OtherTraining(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    briefing_date = db.Column(db.String(15), nullable=False)
    employee_name = db.Column(db.String(80), nullable=False)
    birthdate = db.Column(db.String(15), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    type_of_briefing = db.Column(db.String(40), nullable=False)
    instructor_name = db.Column(db.String(80), nullable=False)
    next_briefing = db.Column(db.String(15), nullable=False)

    def __init__(self, briefing_date, employee_name, birthdate, position,
                 type_of_briefing, instructor_name, next_briefing):
        self.briefing_date = briefing_date
        self.employee_name = employee_name
        self.birthdate = birthdate
        self.position = position
        self.type_of_briefing = type_of_briefing
        self.instructor_name = instructor_name
        self.next_briefing = next_briefing


class Planning(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    employee_name = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    type_of_briefing = db.Column(db.String(40), nullable=False)
    instructor_name = db.Column(db.String(80), nullable=False)
    briefing_date = db.Column(db.String(15), nullable=False)

    def __init__(self, employee_name, position, type_of_briefing, instructor_name, briefing_date):
        self.employee_name = employee_name
        self.position = position
        self.type_of_briefing = type_of_briefing
        self.instructor_name = instructor_name
        self.briefing_date = briefing_date


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# {% extends 'base.html' %}
# {% block title %} Home {% endblock %}
# {% block body %}
#
# <div class="container">
#     <div class="row">
#         <div class="col-md-6 col-md-offset-3 well">
#             <h3 class="text-center">Авторизация</h3>
#             {% with messages = get_flashed_messages() %}
#             {% if messages %}
#             <ul class=flashes>
#                 {% for message in messages %}
#                 <li>{{ message }}</li>
#                 {% endfor %}
#             </ul>
#             {% endif %}
#             {% endwith %}
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
#                     <a class="btn btn-primary" href="{{ url_for('register') }}">Регистрация</a>
#                     <input class="btn btn-primary" type="submit" value="Авторизоваться">
#                     <input type="checkbox" name="remainme" value="Остаться в системе">
#                 </div>
#             </form>
#         </div>
#     </div>
# </div>
# {% endblock %}