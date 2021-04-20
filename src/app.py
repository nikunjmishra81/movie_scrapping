

# import logging

from flask import Flask
from src.config import APP_PORT
from src.routes import db_route_prefix
from src.routes.db_route import db_endpoint
from src.config import DB_URL
from src.models import db
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

app.register_blueprint(db_endpoint, url_prefix=db_route_prefix)
if __name__ == "__main__":
    app.run(host = 'localhost', port=APP_PORT)
