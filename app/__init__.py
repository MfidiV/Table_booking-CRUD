from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from .db import db 
import os

def create_app():
    #Load environment variables from a .env file
    load_dotenv()

    #Initialize the Flask app
    app = Flask(__name__)

    # Set configuration values from the environment
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY') 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    # Import and register the main Blueprint containing routes
    from .routes import main
    app.register_blueprint(main)
   
    """Define a custom CLI command to initialize the database
    Create all tables defined in your SQLAlchemy models"""
    @app.cli.command("init-db")
    def init_db():
        with app.app_context():
            db.create_all()  
            print("Database initialized.")

    #Return the configured app instance
    return app
