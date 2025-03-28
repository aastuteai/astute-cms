import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv  

load_dotenv()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)  
    
    app.config['SECRET_KEY'] = 'astuteai123'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("neon_blog_db") 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    from .views import views
    from .auth import auth 
    from .api import api

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(api, url_prefix='/api/')

    from .models import User  
    with app.app_context():
        db.create_all()  

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    return app
