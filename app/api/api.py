from flask import request, Blueprint
from utils.validation import filter_requests, parameters

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/v1/resources/text', methods=["GET"])
def api_text():
	args = filter_requests(request.args, parameters["text_parameters"])
	print(args)
	return args


@api_bp.route('/api/v1/resources/social', methods=["GET"])
def api_user_platform():
	args = filter_requests(request.args, parameters["user_platform_parameters"])
	print(args)
	return args

