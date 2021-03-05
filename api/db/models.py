from enum import unique
from os import execve, stat
from mongoengine import Document
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import *
import datetime
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# class roles(Document):
#     grants = DynamicField()
#     hierarchy = DynamicField()
#     name = DynamicField()
#     description = DynamicField()
#     normalized = DynamicField()
    
#     def payload(self):
#         return {
#             "id" : str(self.id),
#             "name" : self.name
#         }

class Sample(Document):
    name = StringField()
    
    def payload(self):
        return {
            'id' : str(self.id),
            'name' : self.name
        }