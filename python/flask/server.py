from flask import Flask, render_template, make_response, request, jsonify, abort
from blueprint1 import bp1
from cookies import cbp
import sys

from logger import log_info

app = Flask(__name__, static_folder="static", template_folder="templates")

app.register_blueprint(bp1)
app.register_blueprint(cbp)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/json", methods=["POST"])
def return_json():
    data = request.json
    log_info("get json")
    log_info(data)
    return jsonify([{"test1":1, "test2":2}, {"a":"a1","b":"b1","c":"c1"}])

@app.route("/request_data", methods=["GET"])
def get_request_data():
    log_info("host_url: "+request.host_url)
    log_info("root_url: "+request.root_url)
    log_info("host: "+request.host)
    
    return make_response()

@app.route("/get_value/<value>", methods=["GET"])
def get_from_url(value):
    log_info("value is "+str(value))
    return make_response()

@app.route("/jsonify_code/<code>",methods=["GET"])
def jsonify_code(code=0):
    log_info("this is in jsonify_code:code={}".format(code))
    code=int(code)
    if code==0:
        log_info("in code=0")
        return jsonify({"code":code})
    elif code==1:
        log_info("in code=1")
        return jsonify({"code":code}), 200+code
    else:
        return make_response()

@app.route("/request_test", methods=["GET", "POST"])
def request_test():
    if request.method == "GET":
        log_info("this is GET method")
    elif request.method == "POST":
        log_info("this is POST method")
    else:
        log_info("this is other method:{}".format(request.method))
    log_info("args:{}".format(request.args))
    return make_response()

@app.route("/jsonify_type",methods=["GET"])
def jsonify_type():
    print(type(jsonify({"test":1})))
    return make_response()

@app.route("/post_zero",methods=["POST"])
def post_zero():
    data = request.get_json()
    print("data:{}".format(data))
    if data:
        print("True")
    else:
        print("False")
    return jsonify({"msg":"success"})

@app.route("/raise_exception",methods=["GET"])
def raise_exception():
    try:
        a=1
        raise Exception
    except Exception:
        log_info(sys.exc_info()[0])
        log_info("type:{}".format(str(sys.exc_info()[0])))
        log_info("type:{}".format(type(list)))
        return jsonify(code=1, msg=type(list))

@app.route("/test_abort")
def test_abort():
    abort(500, "test abort")

@app.route("/other_page")
def other_page():
    return render_template("other_page.html",msg="this is other page.")

@app.route("/return_code/<int:code>")
def return_code(code):
    return jsonify({"msg":str(code)}),code

@app.route("/get_json",methods=["POST"])
def get_json():
    data = request.get_json()
    return jsonify(data), 200
#@app.errorhandler(500)
#def show_errorpage(e):
#    msg = "httpステータス:{}, メッセージ:{}, 詳細:{}".format(e.code, e.name, e.description)
#    return render_template("error.html",msg=msg)
if __name__ == "__main__":
    app.run(debug=True, port=5020)