from dataclasses import dataclass
from ..models import db
from sqlalchemy.orm import relationship


@dataclass
class WarpSkill(db.Model):
    __tablename__ = 'warp_skills'
    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String)
    image:str = db.Column(db.String)
    slot1:int = db.Column(db.Integer)
    slot2:int = db.Column(db.Integer)