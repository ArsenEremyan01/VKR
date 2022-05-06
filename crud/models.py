from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


class InductionTraining(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    briefing_date = db.Column(db.String(15), nullable=False)
    employee_name = db.Column(db.String(80), nullable=False)
    birthdate = db.Column(db.String(15), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    subdivision = db.Column(db.String(50), nullable=False)
    instructor_name = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, briefing_date, employee_name, birthdate, position,
                 subdivision, instructor_name, user_id):
        self.briefing_date = briefing_date
        self.employee_name = employee_name
        self.birthdate = birthdate
        self.position = position
        self.subdivision = subdivision
        self.instructor_name = instructor_name
        self.user_id = user_id


class OtherTraining(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    briefing_date = db.Column(db.String(15), nullable=False)
    employee_name = db.Column(db.String(80), nullable=False)
    birthdate = db.Column(db.String(15), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    type_of_briefing = db.Column(db.String(40), nullable=False)
    instructor_name = db.Column(db.String(80), nullable=False)
    next_briefing = db.Column(db.String(15), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, briefing_date, employee_name, birthdate, position,
                 type_of_briefing, instructor_name, next_briefing, user_id):
        self.briefing_date = briefing_date
        self.employee_name = employee_name
        self.birthdate = birthdate
        self.position = position
        self.type_of_briefing = type_of_briefing
        self.instructor_name = instructor_name
        self.next_briefing = next_briefing
        self.user_id = user_id


class Planning(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    employee_name = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    type_of_briefing = db.Column(db.String(40), nullable=False)
    instructor_name = db.Column(db.String(80), nullable=False)
    briefing_date = db.Column(db.String(15), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, employee_name, position, type_of_briefing, instructor_name, briefing_date, user_id):
        self.employee_name = employee_name
        self.position = position
        self.type_of_briefing = type_of_briefing
        self.instructor_name = instructor_name
        self.briefing_date = briefing_date
        self.user_id = user_id


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    ind_tr = db.relationship("InductionTraining")
    oth_tr = db.relationship("OtherTraining")
    plan = db.relationship("Planning")
