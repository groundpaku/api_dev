from models.database import db


class M010User(db.Model):
    __tablename__ = 'm010_user'

    id = db.Column('id', db.VARCHAR(10), primary_key=True)
    name = db.Column('name', db.TEXT)
    birthday = db.Column('birthday', db.TEXT)
    address = db.Column('address', db.TEXT)
    deptcode = db.Column('deptcode', db.TEXT)