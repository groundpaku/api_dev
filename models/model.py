from models.database import db


class M010User(db.Model):
    __tablename__ = 'm010_user'

    id = db.Column('id', db.VARCHAR(10), primary_key=True)
    name = db.Column('name', db.TEXT)
    birthday = db.Column('birthday', db.TEXT)
    address = db.Column('address', db.TEXT)
    deptcode = db.Column('deptcode', db.TEXT)

class T010LoginBonus(db.Model):
    __tablename__ = 't010_login_bonus'

    id = db.Column('id', db.VARCHAR(10), primary_key=True)
    login_count = db.Column('login_count', db.INTEGER)
    last_login_date = db.Column('last_login_date', db.DATETIME)
    login_point = db.Column('login_point', db.INTEGER)
    point_expiry_date = db.Column('point_expiry_date', db.DATETIME)