from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    model = db.Column(db.String)
    rank = db.Column(db.String)
    genzone = db.Column(db.String)
    element = db.Column(db.String)
    image = db.Column(db.String)


@app.route("/")
def home(): 
    character_list = db.session.query(Character).all()
    return render_template("home.html", character_list=character_list)

@app.post("/add")
def add(): 
    character = Character(
        name = request.form.get("name"),
        model = request.form.get("model"),
        rank = request.form.get("rank"),
        genzone = request.form.get("genzone"),
        element = request.form.get("element"),
        image = request.form.get("image")
    )
    db.session.add(character)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    # Start the Flask application
    app.run(debug=True)