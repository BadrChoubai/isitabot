from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/api/v1/resources/text')
def api_index():
    return ""

@app.route('/api/v1/resources/social/:user/:platform')
def api_user_platform():
    return ""
