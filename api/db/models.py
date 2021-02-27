from enum import unique
from os import execve, stat
from mongoengine import Document
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import *
import datetime
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Sample(Document):
    name = StringField(required=True)

    def payload(self):
        return {
            "id" : str(self.id),
            "name" : self.name,
        }
    