import os
import sys
from logging import handlers
from flask import Flask, request, jsonify
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

# @app.route("/")
# def hello():
#     app.logger.info("hello")
#     return "Hello World!"

# @app.route("/db")
# def db_access():
#     try:
#         data_list = []
#         # DB接続
#         engine = create_engine(
#                f"postgresql://chat_user01:Chat@172.20.63.23/chat_tto"
#             )
#         # セッション作成
#         factory = sessionmaker(bind=engine)
#         session = factory()

#         # データ検索
#         for instance in session.query(M010User):
#             dict_user = {"id": instance.id,
#                          "name": instance.name,
#                          "birthday": instance.birthday,
#                          "address": instance.address,
#                          "deptcode": instance.deptcode}
#             data_list.append(dict_user)
    
#         return data_list
#     except Exception as e:
#         return str(e)

# @app.route("/login", methods=['POST'])
# def login():
#     app.logger.info("/login start.")
#     dict_login_user = request.get_json()
    
#     try:
#         # DB接続
#         engine = create_engine(
#                f"postgresql://chat_user01:Chat@172.20.63.23/chat_tto"
#             )
#         # セッション作成
#         factory = sessionmaker(bind=engine)
#         session = factory()

#         # データ検索
#         instance = session.query(M010User).filter(M010User.name == dict_login_user["name"]).first()
#         if instance is not None:
#             dict_user = {"id": instance.id,
#                          "name": instance.name,
#                          "birthday": instance.birthday,
#                          "address": instance.address,
#                          "deptcode": instance.deptcode}
#             app.logger.info("User is" + str(dict_user))
#             return jsonify(dict_user), 201
#         else:
#             app.logger.info("User does not exist. [name:" + str(dict_login_user["name"]) + "]")
#             return "User does not exist.", 200
#     except Exception as e:
#         app.logger.error(e)
#         return str(e)


app.register_blueprint(api_01_login.app, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=Config.DEBUG, host=Config.SERVER_ADDR, port=Config.SERVER_PORT)
