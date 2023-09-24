#!/usr/bin/env python3
from flask import Flask
from models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SECRET_KEY"] = "ghjkjhgffghjhgfd-fghjkjhgfd-ytreiuyt=vbnm876dfgh"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizza_resturant.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False
migrate = Migrate(app, db)
db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    
    