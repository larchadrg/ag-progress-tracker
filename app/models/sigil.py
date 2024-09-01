from dataclasses import dataclass
from ..models import db
from sqlalchemy.orm import relationship

@dataclass
class Sigil(db.Model):
    __tablename__ = 'sigils'
    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String)
    image:str = db.Column(db.String)