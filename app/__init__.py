import os

from flask import Flask, render_template, request
from werkzeug.datastructures import ImmutableMultiDict
from app.api.api import api_bp

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(api_bp)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/')
    def index():
        return render_template("index.html")


    @app.route('/comment-demo')
    def comment_demo():
        return render_template("comment-demo.html")


    @app.route('/user-platform-demo')
    def user_platform_demo():
        data = {"options": [{"name": "Twitter", "icon_class": "bi-twitter"},
                            {"name": "Reddit", "icon_class": "bi-reddit"}]}
        return render_template("user-platform-demo.html", data=data)


    @app.route('/about')
    def about():
        return render_template("about.html")


    return app

