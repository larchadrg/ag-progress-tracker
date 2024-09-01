from flask import Blueprint, jsonify, render_template
from ..models import db
from ..models.sigil import Sigil  # Importa el modelo Sigil

# Crear Blueprint para las rutas de sigilos
sigil_bp = Blueprint('sigil_bp', __name__)

@sigil_bp.get("/api/sigils")
def list_sigils():
    sigil_list = db.session.query(Sigil).all()
    return jsonify(sigil_list)

@sigil_bp.get("/api/sigil/<int:id>/image")
def sigil_image(id):
    sigil = db.session.query(Sigil).filter(Sigil.id == id).first()
    return render_template("image.html", image=sigil.image)
