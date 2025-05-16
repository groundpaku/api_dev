#! /usr/bin/python3
# coding: utf-8

import os
import datetime

# from config import config
# from constants import Constants

from models.database import db
from models.model import M010User

from flask import Blueprint, request, jsonify, current_app
from flask_restful import Resource, Api

app = Blueprint("04_login", __name__)
api = Api(app)

SYSTEM_ID = "Api01Login"
session = db.session


class Api01Login(Resource):
    """
    ログイン
    """
    
    def __init__(self):
        self.logger = current_app.logger
        # self.config = config[os.getenv("FLASK_CONFIG") or "default"]

    def post(self):
        self.logger.info(SYSTEM_ID + " start.")
        dict_login_user = request.get_json()
        
        try:
            # # DB接続
            # engine = create_engine(
            #        f"postgresql://chat_user01:Chat@172.20.63.23/chat_tto"
            # )
            # # セッション作成
            # factory = sessionmaker(bind=engine)
            # session = factory()

            # データ検索
            instance = session.query(M010User).filter(M010User.name == dict_login_user["name"]).first()
            if instance is not None:
                dict_user = {"id": instance.id,
                             "name": instance.name,
                             "birthday": instance.birthday,
                             "address": instance.address,
                             "deptcode": instance.deptcode}
                self.logger.info("User is " + str(dict_user))
                print(dict_user)
                response = jsonify(dict_user)
                response.status_code = 201
                return response
            else:
                self.logger.info("User does not exist. [name:" + str(dict_login_user["name"]) + "]")
                return "User does not exist.", 200
        except Exception as e:
            self.logger.error(e)
            return str(e)
    
        
# ここにURLとの対応を記述
api.add_resource(Api01Login, "/01_login")
