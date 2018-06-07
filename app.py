from chalice import Chalice, Response

app = Chalice(app_name='meowapi')


##
#	EXAMPLES 
##

@app.route('/')
def index():
	return {'hello': 'world'}

@app.route('/hello/{name}')
def hello(name):
	if name == "" or name==None:
		return Response(body={"title":"Method Not Allowed","status":405,"detail":"What's your name? If you don't tell me your name, I can't say hello!"},
					status_code=405)
	if name.lower() == "marc":
		return Response(body={"title":"Method Not Allowed","status":405,"detail":"Sorry, this firstname is not accepted here. ;)"},
					status_code=405)
	return Response(body={'message': {'text': "Hello "+name}},
					status_code=200)


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
