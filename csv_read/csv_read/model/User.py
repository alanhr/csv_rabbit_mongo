from mongoengine import Document, EmailField, StringField, IntField


class User(Document):
    email = EmailField(required=True, unique=True)
    name = StringField(required=True, min_length=3)
    age = IntField(required=True, min_value=1)
