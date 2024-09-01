from flask import Blueprint, jsonify, render_template
from sqlalchemy import or_, and_
from ..models import db
from ..models.character import Character  # Importa el modelo Character
from ..models.sigil import Sigil  # Importa otros modelos según sea necesario
from ..models.warp_skill import WarpSkill
from ..models.rank import Rank
from ..models.functor import Functor
from ..models.element import Element

# Crear Blueprint para las rutas de personajes
character_bp = Blueprint('character_bp', __name__)

@character_bp.route("/")
def home():
    regions = db.session.query(Character.genzone).distinct()
    region_list = [row[0] for row in regions]
    elements = db.session.query(Element.name).distinct()
    elements = [row[0] for row in elements]
    progress_labels = ["Not Started", "In Progress", "Completed"]
    return render_template("home.html", regions=region_list, elements=elements, progress_labels=progress_labels)

@character_bp.get("/api/characters-info")
def list_characters():
    character_list = db.session.query(Character).order_by(Character.name).all()
    characters_json = []

    for character in character_list:
        character_dict = {
            "id": character.id,
            "name": character.name,
            "model": character.model,
            "rank": character.rank,
            "genzone": character.genzone,
            "image": character.image,
            "elements": [element.name for element in character.elements]
        }
        characters_json.append(character_dict)

    return jsonify(characters_json)

@character_bp.route("/character/<int:id>")
def character_info(id):
    character = db.session.query(Character).filter(Character.id == id).first()
    sigils = db.session.query(Sigil).order_by(Sigil.name).all()
    warp_skills = db.session.query(WarpSkill).order_by(WarpSkill.name).all()
    ranks = db.session.query(Rank).all()
    selectable_functors = db.session.query(Functor).filter(
        or_(
            and_(Functor.main_character_id == None, Functor.faction == character.genzone),
            Functor.main_character_id == character.id
        )
    ).all()

    return render_template("character.html", character=character, sigils=sigils,
                           warp_skills=warp_skills, ranks=ranks, functors=selectable_functors)
