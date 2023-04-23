from flask import Flask, render_template, make_response, request, jsonify, abort
from basic.blueprint1 import bp1
from basic.cookies import cbp
from basic.basic import basic_blueprint
#from login.login import login_blueprint
import sys
from flask_sqlalchemy import SQLAlchemy

from basic.logger import log_info
#from login.login import init_login

app = Flask(__name__, static_folder="static", template_folder="basic/templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.secret_key = 'super secret string'
app.register_blueprint(bp1)
app.register_blueprint(cbp)
app.register_blueprint(basic_blueprint)
#app.register_blueprint(login_blueprint)

#db = SQLAlchemy(app)
#app.extentions["db"] = db

#init_login(app)
@app.route("/")
def index():
    return render_template("basic/index.html")

#@app.errorhandler(500)
#def show_errorpage(e):
#    msg = "httpステータス:{}, メッセージ:{}, 詳細:{}".format(e.code, e.name, e.description)
#    return render_template("error.html",msg=msg)

@app.route("/test/<string:tes>")
def test(tes=""):
    print()
if __name__ == "__main__":
    app.run(debug=True, port=5020)