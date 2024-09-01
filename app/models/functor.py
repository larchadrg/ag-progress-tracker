from dataclasses import dataclass
from ..models import db
from sqlalchemy.orm import relationship

@dataclass
class Functor(db.Model): 
    __tablename__ = 'functors'
    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String)
    faction:str = db.Column(db.String)
    rarity:str = db.Column(db.String)
    main_character_id:int = db.Column(db.Integer, db.ForeignKey('characters.id'))
    image:str = db.Column(db.String)
    character = relationship("Character", back_populates="functors")

