
from flask import Blueprint,current_app,request
from flask_login import login_user, logout_user
from flask_login import LoginManager
from login.models import User
login_blueprint = Blueprint("login",__name__,url_prefix="/login",template_folder="templates")

@login_blueprint.route("/login",methods=["GET","POST"])
def login():
    data = request.form
    email = data["email"]
    password = data["password"]
    if valid():
        login_user(user)
        return redirect(request.args.get('next') or url_for('index'))

@login_manager
def load_user(user_id):
    return User.get(user_id)


def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    app.extentions["login_manager"] = login_manager