from flask import Flask
from flask_login import LoginManager
from crud.models import db, User
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
csrf = CSRFProtect(app)
app.app_context().push()
app.secret_key = "inSpo_Eremyan2001-KubGu090601"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:arsen@localhost/vkr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
db.create_all()

from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
