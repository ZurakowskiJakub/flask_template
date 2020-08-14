# Jakub's Flask Server App Template
A simple Flask application, distributed into multiple folders.

Supports the following:
1. Modularity
2. Environment Config
3. Logging
4. MongoDB

## Installation
1. Create a python virtual environment `python -m venv .`
2. Install required packages / modules `pip install requirements.txt`
3. Add a `.env` file
   1. This file should have the below (check `src.config.config`) for the full list in case I forgot to update the README

```
FLASK_ENV = Local | Development | Production
FLASK_DEBUG = True | False
FLASK_TESTING = True | False
FLASK_SECRET_KEY = # A really long hard-to-guess text

# Mongo DB URL / URI
MONGO_URI = mongodb+srv://{user_name}:{password}@main.tydga.mongodb.net/{database}?retryWrites=true&w=majority

# 0=All, 10=Debug+, 20=Info+, 30=Warning+, 40=Error+, 50=Critical
LOGGING_LEVEL = 0 | 10 | 20 | 30 | 40 | 50
```

## License
Please see License.md