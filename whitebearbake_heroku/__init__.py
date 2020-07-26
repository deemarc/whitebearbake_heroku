from flask import Flask, jsonify, Response
from flask_cors import CORS

def create_app(cfg=None):
    """ Define the app object and instantiate context """
    # Instantiate app object
    app = Flask(__name__)
    # Instantiate CORS
    CORS(app)
    # api routes

    from whitebearbake_heroku.api import bp as api
    app.register_blueprint(api, url_prefix='/api')

    # UI routes
    from whitebearbake_heroku.ui import bp as ui
    app.register_blueprint(ui, url_prefix='/')

    app.app_context().push()
    
    return app