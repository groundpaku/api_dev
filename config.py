import logging

class Config:
    # デバッグフラグ
    DEBUG = True
    # ログレベル
    LOGLEVEL = logging.DEBUG
    # API待受ポート
    SERVER_PORT = 8080
    # ログファイル名
    LOGFILE = "/var/log/api/api.log"
    # ログ書式
    LOGFORMATTER = logging.Formatter("%(asctime)s: %(threadName)s[%(levelname)-7s] %(message)s")
    # ログ最大サイズ
    LOGMAXSIZE = 104857600
    # ログバックアップ保持数
    LOGBACKUPCOUNT = 10
    # DB(MySQL) URL
    DBURL = "postgresql://172.20.63.23:5432/chat_tto?user=chat_user01&password=Chat"
    SQLALCHEMY_DATABASE_URI = DBURL
    # API待受アドレス
    SERVER_ADDR = "0.0.0.0"
    