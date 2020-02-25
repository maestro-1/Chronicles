from flaskblog.models import Post
from flask import render_template, request, Blueprint

main = Blueprint('main', __name__)


@main.route("/home")
@main.route("/")
def home_page():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.asc()).paginate(per_page=5)
    return render_template('home.html', title='Home', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
