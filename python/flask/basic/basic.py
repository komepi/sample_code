
from flask import Blueprint,request,jsonify,make_response,abort,render_template
from .logger import log_info

basic_blueprint = Blueprint("basic",__name__,url_prefix="/basic")

@basic_blueprint.route("/json", methods=["POST"])
def return_json():
    data = request.json
    log_info("get json")
    log_info(data)
    return jsonify([{"test1":1, "test2":2}, {"a":"a1","b":"b1","c":"c1"}])

@basic_blueprint.route("/request_data", methods=["GET"])
def get_request_data():
    log_info("host_url: "+request.host_url)
    log_info("root_url: "+request.root_url)
    log_info("host: "+request.host)
    
    return make_response()

@basic_blueprint.route("/get_value/<string:value>", methods=["GET"])
def get_from_url(value):
    log_info("value is "+str(value))
    return make_response()

@basic_blueprint.route("/jsonify_code/<code>",methods=["GET"])
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
    
@basic_blueprint.route("/request_test", methods=["GET", "POST"])
def request_test():
    if request.method == "GET":
        log_info("this is GET method")
    elif request.method == "POST":
        log_info("this is POST method")
    else:
        log_info("this is other method:{}".format(request.method))
    log_info("args:{}".format(request.args))
    return make_response()

@basic_blueprint.route("/jsonify_type",methods=["GET"])
def jsonify_type():
    print(type(jsonify({"test":1})))
    return make_response()

@basic_blueprint.route("/post_zero",methods=["POST"])
def post_zero():
    data = request.get_json()
    print("data:{}".format(data))
    if data:
        print("True")
    else:
        print("False")
    return jsonify({"msg":"success"})

@basic_blueprint.route("/raise_exception",methods=["GET"])
def raise_exception():
    try:
        a=1
        raise Exception
    except Exception:
        log_info(sys.exc_info()[0])
        log_info("type:{}".format(str(sys.exc_info()[0])))
        log_info("type:{}".format(type(list)))
        return jsonify(code=1, msg=type(list))

@basic_blueprint.route("/test_abort")
def test_abort():
    abort(500, "test abort")

@basic_blueprint.route("/other_page")
def other_page():
    return render_template("other_page.html",msg="this is other page.")

@basic_blueprint.route("/return_code/<int:code>")
def return_code(code):
    return jsonify({"msg":str(code)}),code

@basic_blueprint.route("/get_json",methods=["POST"])
def get_json():
    data = request.get_json()
    return jsonify(data), 200

@basic_blueprint.route("/paths",methods=["GET","POST"])
def paths():
    log_info("request.method:{}".format(request.method))
    log_info("request.url:{}".format(request.url))
    log_info("request.base_url:{}".format(request.base_url))
    log_info("request.url_root:{}".format(request.url_root))
    log_info("request.host_url:{}".format(request.host_url))
    log_info("request.host:{}".format(request.host))
    log_info("request.path:{}".format(request.path))
    log_info("request.full_path:{}".format(request.full_path))
    log_info("request.args:{}".format(request.args))
    return make_response()