from flask import Blueprint, render_template, current_app

blueprint=Blueprint(
    'root_blueprint',
    __name__,
    template_folder='templates',
    static_folder='static',
)

@blueprint.route("/")
def index():
    current_app.logger.debug("called index")
    return render_template("index.html")