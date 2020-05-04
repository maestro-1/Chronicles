import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from .config import BaseConfig
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(BaseConfig)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

mail = Mail(app)
migrate = Migrate(app, db)

from flaskblog.main.routes import main
from flaskblog.Users.routes import users
from flaskblog.Posts.routes import posts
from flaskblog.errors.handlers import errors


app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(errors)
# https://www.youtube.com/watch?v=qWYw_Bd1FHo
