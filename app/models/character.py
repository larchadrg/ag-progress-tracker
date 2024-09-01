from dataclasses import dataclass
from ..models import db
from sqlalchemy.orm import relationship

@dataclass
class Character(db.Model):
    __tablename__ = 'characters'
    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String)
    model:str = db.Column(db.String)
    rank:str = db.Column(db.String)
    genzone:str = db.Column(db.String)
    image:str = db.Column(db.String)
    elements = relationship("Element", back_populates="character")
    has_synergy_weapon:int = db.Column(db.Integer)
    functors = relationship("Functor", back_populates="character")
