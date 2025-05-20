#! /usr/bin/python3
# coding: utf-8

import datetime
from models.database import db
from models.model import M010User, T010LoginBonus

from flask import Blueprint, request, jsonify, current_app
from flask_restful import Resource, Api

app = Blueprint("03_update_login_bonus", __name__)
api = Api(app)

SYSTEM_ID = "Api03UpdateLoginBonus"
session = db.session


class Api03UpdateLoginBonus(Resource):
    """
    ログインボーナス更新(加算・除算)
    """
    
    def __init__(self):
        self.logger = current_app.logger

    def post(self):
        self.logger.info(SYSTEM_ID + " start.")
        dict_login_user = request.get_json()
        
        try:
            # データ検索
            instance = session.query(T010LoginBonus).filter(T010LoginBonus.id == dict_login_user["id"]).first()
            if instance is not None:
                # データが存在する場合
                # パラメータにより処理を分岐
                datetime_today = datetime.datetime.today()
                str_process_kbn = dict_login_user["process_kbn"]
                if str_process_kbn == "0":
                    # 加算(ログインボーナス取得)
                    instance.last_login_date = datetime_today
                    instance.login_count += 1
                    instance.login_point += 1
                    instance.point_expiry_date += datetime_today + datetime.timedelta(days=365)
                else:
                    # 除算(ログインボーナス使用)
                    instance.login_count = 0
                    instance.login_point = 0
                    instance.point_expiry_date = None

                response = jsonify({"result": True, "error_msg": ""})
                response.status_code = 201
                self.logger.info(SYSTEM_ID + " true.")
                return response
            else:
                # データが存在しない場合
                self.logger.info("User does not exist. [id:" + str(dict_login_user["id"]) + "]")
                self.logger.info(SYSTEM_ID + " false.")
                return "User does not exist.", 200
        except Exception as e:
            self.logger.error(e)
            self.logger.info(SYSTEM_ID + " false.")
            return str(e)
    
        
# ここにURLとの対応を記述
api.add_resource(Api03UpdateLoginBonus, "/03_update_login_bonus")
