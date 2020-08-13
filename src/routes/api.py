from flask import Blueprint

api_module = Blueprint('api', __name__, url_prefix='/api')


@api_module.route('/')
def api_index():
    return {"let's pretend this is json": "yes"}
