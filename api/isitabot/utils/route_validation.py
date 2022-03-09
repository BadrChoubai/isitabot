from werkzeug.datastructures import ImmutableMultiDict

parameters = {
	"text_parameters": [
		"encoded_text"
	],
	"user_platform_parameters": [
		"username",
		"platform"
	]
}


def filter_requests(
received_data: ImmutableMultiDict,
parameters: list[str]
) -> dict:
	# https://stackoverflow.com/questions/50396370/multiple-queries-in-one-elasticsearch-query
	# Used for matching on multiple parameters at a time.
	"""Returns a dictionary containing all request parameters."""
	parameter_list = [(key, received_data.get(key)) for key in parameters]
	return {key: value for key, value in parameter_list if value}

