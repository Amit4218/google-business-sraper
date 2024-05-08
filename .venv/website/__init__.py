from flask import Flask
from .views import views
from .models import models
from dotenv import load_dotenv
import os
from flask_cors import CORS


def create_app():
    load_dotenv()

    app = Flask(__name__)
    
    CORS(app)
    
     
    app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

    app.secret_key = 'TEST'

    app.register_blueprint(views)
    app.register_blueprint(models)

    return app
