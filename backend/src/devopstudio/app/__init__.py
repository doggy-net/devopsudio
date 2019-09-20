from flask import Flask

from . import api, index


def create_app():
    app = Flask(__name__,
                static_folder='dist',
                static_url_path='',
                template_folder='dist')
    app.register_blueprint(api.bp)
    app.register_blueprint(index.bp)
    return app
