from limberframework.database.models import Model
from sqlalchemy import Column, Integer, String, ForeignKey

class User(Model):
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    soft_delete = True

class ApiKey(Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    key = Column(String)
