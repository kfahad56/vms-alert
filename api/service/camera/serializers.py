from typing import Optional, List
from mongoengine.fields import EmailField
from pydantic import BaseModel

class VMS(BaseModel):
    image : str
