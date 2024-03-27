from flask import Flask

from index import blueprint as root_blueprint
app = Flask(__name__)

app.register_blueprint(root_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)