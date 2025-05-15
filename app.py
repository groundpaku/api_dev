from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import M010User

app = Flask(__name__)

@app.route("/")
def hello():
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
    


if __name__ == "__main__":
    app.run()
