from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ed576332c78752f352dc0826ef34945b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog.main.routes import main
from flaskblog.Users.routes import users
from flaskblog.Posts.routes import posts


app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(posts)

# https://www.youtube.com/watch?v=qWYw_Bd1FHo
