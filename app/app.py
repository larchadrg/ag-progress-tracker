from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
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

@app.route("/")
def home(): 
    return render_template("home.html")

@app.get("/api/characters-info") 
def list_characters(): 
    character_list = db.session.query(Character).all()
    return jsonify(character_list)

@app.route("/character/<int:id>")
def character_info(id):
    character = db.session.query(Character).filter(Character.id == id).first()
    sigils = db.session.query(Sigil).all()
    return render_template("character.html", character=character, sigils = sigils)

@app.get("/api/sigils")
def list_sigils(): 
    sigil_list = db.session.query(Sigil).all()
    return jsonify(sigil_list)

@app.get("/api/sigil/<int:id>/image")
def sigil_image(id): 
    sigil = db.session.query(Sigil).filter(Sigil.id == id).first()
    return render_template("image.html", image = sigil.image)

if __name__ == "__main__":
    # Start the Flask application
    app.run(debug=True)