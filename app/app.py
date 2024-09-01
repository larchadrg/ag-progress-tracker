from flask import Flask
import os 
from .db_manager.create_db import create_database
from .db_manager.load_db import load_ag_data
from .models import db
from .routes import init_routes  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(app.root_path, "instance/database.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    create_database()
    load_ag_data()

init_routes(app)

if __name__ == "__main__":
    # Start the Flask application
    app.run(debug=True)