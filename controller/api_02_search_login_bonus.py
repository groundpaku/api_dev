#! /usr/bin/python3
# coding: utf-8

import datetime

from models.database import db
from models.model import M010User, T010LoginBonus

from flask import Blueprint, request, jsonify, current_app
from flask_restful import Resource, Api

app = Blueprint("02_search_login_bonus", __name__)
api = Api(app)

SYSTEM_ID = "Api02SearchLoginBonus"
session = db.session


class Api02SearchLoginBonus(Resource):
    """
    ログインボーナス情報取得
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
                dict_user = {"id": instance.id,
                             "login_count": instance.login_count,
                             "last_login_date": instance.last_login_date,
                             "login_point": instance.login_point,
                             "point_expiry_date": instance.point_expiry_date}
                self.logger.info("User is " + str(dict_user))
                # ログインボーナス取得対象者か判断
                datetime_today = datetime.datetime.today()
                datetime_diff = datetime_today - instance.last_login_date
                self.logger.info(datetime_diff)
                str_login_bonus_flg = "0" # 0:非対象者 1:対象者
                if datetime_diff.days > 1:
                    str_login_bonus_flg = "1"

                dict_result = {"result": True, "error_msg": "",
                               "login_bonus_flg": str_login_bonus_flg,
                               "user_info": dict_user}
                self.logger.info(dict_result)
                response = jsonify(dict_result)
                response.status_code = 201
                self.logger.info(SYSTEM_ID + " true.")
                return response
            else:
                self.logger.info("User does not exist. [id:" + str(dict_login_user["id"]) + "]")
                self.logger.info(SYSTEM_ID + " false.")
                return "User does not exist.", 200
        except Exception as e:
            self.logger.error(e)
            self.logger.info(SYSTEM_ID + " false.")
            return str(e)
    
        
# ここにURLとの対応を記述
api.add_resource(Api02SearchLoginBonus, "/02_search_login_bonus")
