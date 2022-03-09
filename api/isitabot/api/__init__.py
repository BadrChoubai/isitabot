from flask import request, Blueprint
from isitabot.utils.route_validation import filter_requests, parameters
# import isitabot.ML.LM_probabilities as LM_probabilities
# import isitabot.ML.analyze as analyze
# from isitabot.ML.models_gen import models

bp = Blueprint('api', __name__)


@bp.route('/api/v1/resources/text', methods=["GET"])
def api_text():
    args = filter_requests(request.args, parameters["text_parameters"])
    # print(form['encoded_text'])
    # result = analyze.interpret_result(analyze.estimate_sample(
    #     LM_probabilities.run_all_tests(args['encoded_text'], models)))
    # send text to probs
    return args 


# @bp.route('/api/v1/resources/social', methods=["GET"])
# def api_user_platform():
#     args = filter_requests(
#         request.args, parameters["user_platform_parameters"])
#     return args
