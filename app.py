from flask import Flask

from src.routes.api import api_module
from src.routes.app import app_module

app = Flask(__name__)

app.config.from_object('src.config.config.Config')
app.register_blueprint(api_module)
app.register_blueprint(app_module)


if __name__ == "__main__":
    app.run(debug=True)
else:
    app.run()
