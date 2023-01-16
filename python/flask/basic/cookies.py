from flask import Blueprint, make_response, request, jsonify
from .logger import log_info
import json

cbp = Blueprint('cookie',
                __name__,
                url_prefix='/cookie')

@cbp.route("/value")
def count_cookie():
    cookie = request.cookies.get("count", None)
    if cookie:
        log_info("cookie: "+str(cookie))
        cookie=str(int(cookie)+1)
    else:
        log_info("cookie: None")
        cookie=str(1)
    log_info(cookie)
    response = make_response()
    response.set_cookie("count", value=cookie)
    return response

@cbp.route("/dict")
def dict_cookie():
    cookie = request.cookies.get("dict",None)
    response = make_response()
    
    if cookie:
        dic = json.loads(cookie)
        log_info("now cookie")
        log_info(dic)
        
        dic["key"+str(len(dic)+1)]="val"+str(len(dic)+1)
        response.set_cookie("dict",value=json.dumps(dic))
        log_info("after cookie")
        log_info(dic)
    else:
        log_info("not test_json in cookie.")
        res_dic={"key1":"val1","key2":"val2"}
        log_info("set cookie")
        log_info(res_dic)
        response.set_cookie("dict",value=json.dumps(res_dic))
    return response