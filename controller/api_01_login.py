#! /usr/bin/python3
# coding: utf-8

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

    def post(self):
        self.logger.info(SYSTEM_ID + " start.")
        dict_login_user = request.get_json()
        
        try:
            # データ検索
            instance = session.query(M010User).filter(M010User.id == dict_login_user["id"]).first()
            if instance is not None:
                dict_user = {"id": instance.id,
                             "name": instance.name,
                             "birthday": instance.birthday,
                             "address": instance.address,
                             "deptcode": instance.deptcode}
                self.logger.info("User is " + str(dict_user))
                
                response = jsonify(dict_user)
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
api.add_resource(Api01Login, "/01_login")
