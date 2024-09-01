from dataclasses import dataclass
from ..models import db
from sqlalchemy.orm import relationship


@dataclass
class Element(db.Model):
    __tablename__ = 'elements'
    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String)
    character_id:int = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character = relationship("Character", back_populates="elements")
