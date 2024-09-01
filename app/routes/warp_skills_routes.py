from flask import Blueprint, jsonify
from ..models import db
from ..models.warp_skill import WarpSkill  # Importa el modelo WarpSkill

# Crear Blueprint para las rutas de habilidades de distorsión
warp_skill_bp = Blueprint('warp_skill_bp', __name__)

@warp_skill_bp.get("/api/warp-skills")
def list_warp_skills():
    warp_skills = db.session.query(WarpSkill).all()
    return jsonify(warp_skills)
