#!/usr/bin/env python3
from flask import Flask ,make_response
from models import db , Restaurant , Pizza , RestaurantPizza
from flask_migrate import Migrate
from flask_restful import Resource , Api 
from schema import restaurants_schema

app = Flask(__name__)
app.config["SECRET_KEY"] = "ghjkjhgffghjhgfd-fghjkjhgfd-ytreiuyt=vbnm876dfgh"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizza_resturant.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False
migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
class RestaurantResource(Resource):
    def get (self):
        restaurants = Restaurant.query.all()
        response = make_response(restaurants_schema.dumps(restaurants),200)
        return response
        
        
api.add_resource(RestaurantResource,"/restaurants")

class HomeResource(Resource):
    def get (self):
        response = make_response({"Message":"Pizza Restaurant API."},200)
        return response
        
api.add_resource(HomeResource,"/")


if __name__ == '__main__':
    app.run(port=5555, debug=True)
    
    