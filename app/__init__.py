import os

from flask import Flask, request, render_template

from validation import filter_requests, parameters
from api import api_bp
import LM_probabilities
import analyze

models = []

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    # app.register_blueprint(api_bp)

    models = LM_probabilities.get_default_models()

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

    @app.route('/text-analysis', methods=["GET", "POST"])
    def comment_demo():
        if request.method == 'POST':
            form = filter_requests(request.form, parameters["text_parameters"])
            # print(form['encoded_text'])
            result = analyze.interpret_result(analyze.estimate_sample(LM_probabilities.run_all_tests(form['encoded_text'], models)))
            # send text to probs
            return render_template("text-analysis.html", analysis_result=result)
            
        return render_template("text-analysis.html")

    @app.route('/about')
    def about():
        return render_template("about.html")

    return app
