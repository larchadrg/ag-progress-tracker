from dataclasses import dataclass
from ..models import db
from sqlalchemy.orm import relationship

@dataclass 
class Rank(db.Model): 
    __tablename__ = 'ranks'
    name:str = db.Column(db.String)
    value:str = db.Column(db.String, primary_key=True)
