from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select  
from dataclasses import dataclass
import os 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(app.root_path, "instance/database.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@dataclass
class Character(db.Model):
    __tablename__ = 'characters'
    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String)
    model:str = db.Column(db.String)
    rank:str = db.Column(db.String)
    genzone:str = db.Column(db.String)
    element:str = db.Column(db.String)
    image:str = db.Column(db.String)

@dataclass
class Sigil(db.Model):
    __tablename__ = 'sigils'
    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String)
    image:str = db.Column(db.String)

@dataclass
class WarpSkill(db.Model):
    __tablename__ = 'warp_skills'
    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String)
    image:str = db.Column(db.String)
    slot1:int = db.Column(db.Integer)
    slot2:int = db.Column(db.Integer)

@app.route("/")
def home(): 
    regions = db.session.query(Character.genzone).distinct()
    region_list = [row[0] for row in regions]

    elements = [row[0] for row in db.session.query(Character.element).distinct()]
    progress_labels = ["Not Started", "In Progress", "Completed"]
    return render_template("home.html", regions = region_list, elements = elements, progress_labels = progress_labels)

@app.get("/api/characters-info") 
def list_characters(): 
    character_list = db.session.query(Character).order_by(Character.name).all()
    return jsonify(character_list)

@app.route("/character/<int:id>")
def character_info(id):
    character = db.session.query(Character).filter(Character.id == id).first()
    sigils = db.session.query(Sigil).order_by(Sigil.name).all()
    warp_skills = db.session.query(WarpSkill).order_by(WarpSkill.name).all()

    return render_template("character.html", character=character, sigils = sigils,
                            warp_skills = warp_skills)

@app.get("/api/sigils")
def list_sigils(): 
    sigil_list = db.session.query(Sigil).all()
    return jsonify(sigil_list)

@app.get("/api/warp-skills")
def list_warp_skills(): 
    warp_skills = db.session.query(WarpSkill).all()
    return jsonify(warp_skills)

@app.get("/api/sigil/<int:id>/image")
def sigil_image(id): 
    sigil = db.session.query(Sigil).filter(Sigil.id == id).first()
    return render_template("image.html", image = sigil.image)

if __name__ == "__main__":
    # Start the Flask application
    app.run(debug=True)