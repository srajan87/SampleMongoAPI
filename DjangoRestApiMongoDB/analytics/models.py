from mongoengine import *

# Create your models here.

class Accounts(Document):
    account_id = IntField()
    limit = IntField()
    products = ListField(StringField(max_length=80))  
