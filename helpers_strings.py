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

main_string = '''
from flask_migrate import Migrate

from app import create_app
from dal import db

app = create_app(Config)
db.init_app(app)
migrate = Migrate(app, db)
'''

gitignore_string = '''
Lib
Scripts
include
pyvenv.cfg
'''

requirements = '''
alembic==1.7.5
click==8.0.3
colorama==0.4.4
Flask==2.0.2
Flask-Migrate==3.1.0
Flask-SQLAlchemy==2.5.1
greenlet==1.1.2
importlib-metadata==4.8.2
importlib-resources==5.4.0
itsdangerous==2.0.1
Jinja2==3.0.3
Mako==1.1.6
MarkupSafe==2.0.1
SQLAlchemy==1.4.28
Werkzeug==2.0.2
zipp==3.6.0
'''