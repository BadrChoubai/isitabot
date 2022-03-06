from flask import request, Blueprint
from werkzeug.datastructures import ImmutableMultiDict

api_bp = Blueprint('api', __name__)

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


@api_bp.route('/api/v1/resources/text', methods=["GET"])
def api_text():
	args = filter_requests(request.args, text_parameters)
	print(args)
	return args


@api_bp.route('/api/v1/resources/social', methods=["GET"])
def api_user_platform():
	args = filter_requests(request.args, user_platform_parameters)
	print(args)
	return args

