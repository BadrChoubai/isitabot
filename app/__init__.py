import os

from flask import Flask, render_template, request
from werkzeug.datastructures import ImmutableMultiDict

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

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


    text_parameters = [
        "encoded_text"
    ]

    user_platform_parameters = [
        "username",
        "platform"
    ]


    def filter_requests(
        requests: ImmutableMultiDict,
        parameters: list[str]
    ) -> dict:
        # https://stackoverflow.com/questions/50396370/multiple-queries-in-one-elasticsearch-query
        # Used for matching on multiple parameters at a time.
        """Returns a dictionary containing all request parameters."""
        print(requests, parameters)
        parameter_list = [(key, requests.get(key)) for key in parameters]
        return {key: value for key, value in parameter_list if value}


    @app.route('/api/v1/resources/text', methods=["GET"])
    def api_text():
        args = filter_requests(request.args, text_parameters)
        print(args)
        return args


    @app.route('/api/v1/resources/social', methods=["GET"])
    def api_user_platform():
        args = filter_requests(request.args, user_platform_parameters)
        print(args)
        return args


        
    return app

