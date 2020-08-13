from flask import Blueprint

app_module = Blueprint('app', __name__)


@app_module.route('/')
def app_index():
    return "Hello World!"
