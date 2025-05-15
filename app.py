import os
import logging.handlers
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import M010User
import logging
from config import Config

app = Flask(__name__)

app.logger.setLevel(Config.LOGLEVEL)
handler = logging.handlers.RotatingFileHandler(filename=os.path.abspath(
Config.LOGFILE), maxBytes=Config.LOGMAXSIZE, backupCount=Config.LOGBACKUPCOUNT, encoding="utf-8")
handler.setLevel(Config.LOGLEVEL)
handler.setFormatter(Config.LOGFORMATTER)
app.logger.addHandler(handler)

@app.route("/")
def hello():
    app.logger.info("hello")
    return "Hello World!"

@app.route("/db")
def db_access():
    try:
        data_list = []
        # DB接続
        engine = create_engine(
               f"postgresql://chat_user01:Chat@172.20.63.23/chat_tto"
            )
        # セッション作成
        factory = sessionmaker(bind=engine)
        session = factory()

        # データ検索
        for instance in session.query(M010User):
            dict_user = {"id": instance.id,
                         "name": instance.name,
                         "birthday": instance.birthday,
                         "address": instance.address,
                         "deptcode": instance.deptcode}
            data_list.append(dict_user)
    
        return data_list
    except Exception as e:
        return str(e)

@app.route("/login", methods=['POST'])
def login():
    dict_login_user = request.get_json()
    
    try:
        # DB接続
        engine = create_engine(
               f"postgresql://chat_user01:Chat@172.20.63.23/chat_tto"
            )
        # セッション作成
        factory = sessionmaker(bind=engine)
        session = factory()

        # データ検索
        instance = session.query(M010User).filter(M010User.name == dict_login_user["name"]).first()
        if instance is not None:
            dict_user = {"id": instance.id,
                         "name": instance.name,
                         "birthday": instance.birthday,
                         "address": instance.address,
                         "deptcode": instance.deptcode}
        
            return jsonify(dict_user), 201
        else:
            return "User does not exist.", 200
    except Exception as e:
        app.logger.debug(e)
        return str(e)
    
if __name__ == "__main__":
    app.run()
