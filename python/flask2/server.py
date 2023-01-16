from flask import Flask,render_template,request,jsonify

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/post_zero",methods=["POST"])
def post_zero():
    data = request.get_json()
    print("data:{}".format(data))
    if data:
        print("True")
    else:
        print("False")
    return jsonify({"msg":"success"})
if __name__ == "__main__":
    app.run(debug=True, port=5020)