from flask import Flask, render_template, make_response, request, jsonify
from blueprint1 import bp1
from cookies import cbp

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

if __name__ == "__main__":
    app.run(debug=True, port=5020)