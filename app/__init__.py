from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    
    # Registrar rutas
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()
    
    return app