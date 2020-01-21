from flaskblog import app
from flaskblog.models import Post
from flask import render_template, Blueprint


@app.route("/home")
@app.route("/")
def home_page():
    # post = Post.filter_by().paginate(per_page=5)
    posts = Post.query.all()
    return render_template("home.html", title='Home', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
