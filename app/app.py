from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
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


@app.route("/")
def home(): 
    character_list = db.session.query(Character).all()
    return render_template("home.html", character_list=character_list)

@app.get("/api/characters-info") 
def characters_info(): 
    character_list = db.session.query(Character).all()
    return jsonify(character_list)

if __name__ == "__main__":
    # Start the Flask application
    app.run(debug=True)