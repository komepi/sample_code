from flask import Blueprint, make_response
from logger import log_info

bp1 = Blueprint('test',
                __name__,
                url_prefix='/bp'
)

@bp1.route('/get', methods=['GET'])
def test_get():
    log_info("test_get")
    return make_response()

def test_get_rule():
    log_info("test_get_rule")
    return make_response()

bp1.add_url_rule(
    endpoint="test1",
    rule="/test_rule",
    view_func=test_get_rule,
    methods=["GET"]
)