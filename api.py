from flask import request, Blueprint
from validation import filter_requests, parameters
import LM_probabilities
import analyze
import models

api_bp = Blueprint('api', __name__)


@api_bp.route('/api/v1/resources/text', methods=["GET"])
def api_text():
    args = filter_requests(request.args, parameters["text_parameters"])
    # print(form['encoded_text'])
    result = analyze.interpret_result(analyze.estimate_sample(
        LM_probabilities.run_all_tests(args['encoded_text'], models)))
    # send text to probs
    return result


@api_bp.route('/api/v1/resources/social', methods=["GET"])
def api_user_platform():
    args = filter_requests(
        request.args, parameters["user_platform_parameters"])
    print(args)
    return args
