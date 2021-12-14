from flask_migrate import Migrate

from app import create_app
from dal import db

app = create_app(Config)
db.init_app(app)
migrate = Migrate(app, db)