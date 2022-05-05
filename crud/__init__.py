from flask import Flask
from flask_login import LoginManager
from flask_recaptcha import ReCaptcha
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = "inSpo_Eremyan2001-KubGu090601"

# SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:W5w5y599@localhost/vkr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
manager = LoginManager(app)

from crud import models, routes

db.create_all()
