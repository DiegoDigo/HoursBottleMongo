from datetime import datetime
from mongoengine import *

connect("Hours")


class User(Document):
    username = StringField(max_legth=20, required=True, unique=True)
    password = StringField(max_legth=20, required=True)
    email = EmailField(required=True, unique=True)
    created = DateTimeField(default=datetime.now)
    fisrt_name = StringField(max_legth=50, required=True)
    last_name = StringField(max_legth=50, required=True)
    office = StringField(max_legth=50, required=True, unique=True)
