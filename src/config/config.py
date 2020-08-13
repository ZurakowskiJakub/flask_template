import os

from dotenv import load_dotenv


class Config(object):

    def __init__(self):
        load_dotenv()

        expected_env_vars = {
            'FLASK_DEBUG',
            'FLASK_TESTING',
            'FLASK_SECRET_KEY',
            'FLASK_ENV'
        }

        for expected in expected_env_vars:
            if not os.getenv(expected):
                raise ValueError(f"No {expected} set for this application.")

        self.ENV = os.getenv("FLASK_ENV")
        self.DEBUG = True if os.getenv("FLASK_DEBUG") == 'True' else False
        self.TESTING = True if os.getenv("FLASK_TESTING") == 'True' else False
        self.SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
