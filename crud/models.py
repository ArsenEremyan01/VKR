from crud import db


class Accounting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(80), nullable=False)
    udos = db.Column(db.String(30), unique=True, nullable=False)
    podrz = db.Column(db.String(50), nullable=False)
    workpl = db.Column(db.String(50), nullable=False)
    dolj = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    date_pas = db.Column(db.String(50), nullable=False)

    def __init__(self, fio, udos, podrz, workpl, dolj, status, date_pas):
        self.fio = fio
        self.udos = udos
        self.podrz = podrz
        self.workpl = workpl
        self.dolj = dolj
        self.status = status
        self.date_pas = date_pas


class Planning(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    podrz_plan = db.Column(db.String(50), nullable=False)
    goal = db.Column(db.String(100), nullable=False)
    work_plan = db.Column(db.String(50), nullable=False)
    date_plan = db.Column(db.String(20), nullable=False)

    def __init__(self, podrz_plan, goal, work_plan, date_plan):
        self.podrz_plan = podrz_plan
        self.goal = goal
        self.work_plan = work_plan
        self.date_plan = date_plan

        # <td>{{row.id_obj}}</td>
        # <td>{{row.fio}}</td>
        # <td>{{row.udos}}</td>
        # <td>{{row.podrz}}</td>
        # <td>{{row.workpl}}</td>
        # <td>{{row.dolj}}</td>
        # <td>{{row.grade}}</td>
        # <td>{{row.status}}</td>
# class Data(db.Model):
#     id_obj = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     email = db.Column(db.String(100))
#     phone = db.Column(db.String(100))
#
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
