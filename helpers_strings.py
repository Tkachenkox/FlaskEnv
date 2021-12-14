app_string = '''
from flask import Flask
from .BlueprintGroup import BlueprintGroup

def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    return app
'''

blieprint_group_string = '''
from flask import Flask

class BlueprintGroup:

    def __init__(self, url_prefix: str, *blueprints):
        self.url_prefix = url_prefix
        self.blueprints = blueprints

    def register_blueprints(self, app: Flask) -> Flask:
        for blueprint in self.blueprints:
            app.register_blueprint(blueprint, url_prefix=f"/{self.url_prefix}/{blueprint.url_prefix}")
'''

extensions_string = '''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
'''