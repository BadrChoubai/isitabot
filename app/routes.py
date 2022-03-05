from app import app

@app.route('/')
def index():
    return "Isitabot"

@app.route('/about')
def about():
    return "About isitabot"

@app.route('/api/v1/resources/text')
def api_index():
    return "API Index"

@app.route('/api/v1/resources/social/:user/:platform')
def api_user_platform():
    return "API resource $USER $PLATFORM"
