from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/comment-demo')
def comment_demo():
    return render_template("comment-demo.html")

@app.route('/user-platform-demo')
def user_platform_demo():
    return render_template("user-platform-demo.html")

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/api/v1/resources/text')
def api_index():
    return ""

@app.route('/api/v1/resources/social/:user/:platform')
def api_user_platform():
    return ""
