import os
import sys

from logging import handlers
from flask import Flask

from config import Config
from models.database import db, init_db
from controller import api_01_login

sys.path.insert(1, os.path.abspath(os.path.dirname(__file__)))

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# ログの設定
app.logger.setLevel(Config.LOGLEVEL)
handler = handlers.RotatingFileHandler(filename=os.path.abspath(Config.LOGFILE), 
                                               maxBytes=Config.LOGMAXSIZE, 
                                               backupCount=Config.LOGBACKUPCOUNT, 
                                               encoding="utf-8")
handler.setLevel(Config.LOGLEVEL)
handler.setFormatter(Config.LOGFORMATTER)
app.logger.addHandler(handler)

# DB接続の初期化
app.config["SQLALCHEMY_DATABASE_URI"] = Config.DBURL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_db(app)

app.register_blueprint(api_01_login.app, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=Config.DEBUG, host=Config.SERVER_ADDR, port=Config.SERVER_PORT)
