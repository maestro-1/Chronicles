from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ed576332c78752f352dc0826ef34945b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes





# https://www.youtube.com/watch?v=qWYw_Bd1FHo
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/07-User-Account-Profile-Pic/flaskblog
# https://www.peopleperhour.com/freelancer/admin/ahmed_yar-abbasi-web-development-web-scraping-email-xajnyqj
