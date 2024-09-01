from .character_routes import character_bp  # Importa tu blueprint de rutas
from .sigil_routes import sigil_bp
from .warp_skills_routes import warp_skill_bp

def init_routes(app):
    app.register_blueprint(character_bp)
    app.register_blueprint(sigil_bp)
    app.register_blueprint(warp_skill_bp)