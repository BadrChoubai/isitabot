import os

from flask import Flask, request, render_template
from app.api.api import api_bp
from src.utils.validation import filter_requests, parameters

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


    @app.route('/text-demo', methods=["GET", "POST"])
    def comment_demo():
        if request.method == 'POST':
            form = filter_requests(request.form, parameters["text_parameters"])
            return form 

        return render_template("text-demo.html")


    @app.route('/user-platform-demo', methods=["GET", "POST"])
    def user_platform_demo():
        data = {"options": ["Twitter", "Reddit"]}

        if request.method == 'POST':
            form = filter_requests(request.form, parameters["user_platform_parameters"])
            return form 

        return render_template("user-platform-demo.html", data=data)


    @app.route('/about')
    def about():
        return render_template("about.html")


    return app

