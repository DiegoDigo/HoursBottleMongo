from datetime import datetime
import bcrypt
from mongoengine import *

connect("Hours")


class User(Document):
    username = StringField(max_legth=20, required=True, unique=True)
    password = StringField(max_legth=200, required=True)
    email = EmailField(required=True, unique=True)
    created = DateTimeField(default=datetime.now)
    fisrt_name = StringField(max_legth=50, required=True)
    last_name = StringField(max_legth=50, required=True)
    office = StringField(max_legth=50, required=True, unique=True)

    @classmethod
    def create_user(cls, username, password, email, fisrt_name, last_name, office):
        try:
            cls(username=username,
                password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()),
                email=email,
                fisrt_name=fisrt_name,
                last_name=last_name,
                office=office).save()
        except Exception as e:
            raise Exception(e)

    @classmethod
    def login(cls, username, password):
        try:
            user = cls.objects(username=username)
            for u in user:
                print(u)
        except Exception as e:
            raise Exception(e)
