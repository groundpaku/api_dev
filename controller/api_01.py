from flask import Flask, request
from flask_restful import Api, Resource
import copy

# flaskインスタンス作成
api = Flask(__name__)

# flask_restfulのApiインスタンス作成と関連づけ
flask_api = Api(api)

# ディクショナリ
users = [
    {"user_id": "1", "name": "tujimura", "age": 11},
    {"user_id": "2", "name": "mori", "age": 20},
    {"user_id": "3", "name": "shimada", "age": 50},
    {"user_id": "4", "name": "kyogoku", "age": 70}]

# flask_restfulのルーティング
class UserAPI(Resource):
    # 取得
    # HTTPリクエストにクエリパラメータあり
    # 全件取得 or ageフィルタリング
    def get(self):
        age = request.args.get('age')
        if age:
            return list(filter(lambda user: user['age'] == int(age), users))
        return users

    # 登録
    # HTTPリクエストからJSONを受け取る
    # JSONデータを新規登録
    def post(self):
        data = request.get_json()
        res_users = copy.deepcopy(users)
        res_users.append(data)
        return res_users, 201


# エンドポイントとリソースクラスをマッピングする
flask_api.add_resource(UserAPI, '/api_01')