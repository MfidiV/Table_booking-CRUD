from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from .db import db
import os


def create_app():
    # Load environment variables
    load_dotenv()

    app = Flask(__name__)

    # Config from .env
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

def create_app():
    # Load environment variables
    load_dotenv()

    app = Flask(__name__)

    # Config from .env
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    """Define a custom CLI command to initialize the database
    Create all tables defined in your SQLAlchemy models"""
    @app.cli.command("init-db")
    def init_db():
        with app.app_context():
            db.create_all()  
            print("✅ Database initialized.")

    return app

