#!/usr/bin/env python3
from flask import Flask ,make_response,request
from models import db , Restaurant , Pizza , RestaurantPizza 
from flask_migrate import Migrate
from flask_restful import Resource , Api 
from schema import restaurants_schema , restaurant_with_id_schema , pizzas_schema , pizza_schema

app = Flask(__name__)
app.config["SECRET_KEY"] = "ghjkjhgffghjhgfd-fghjkjhgfd-ytreiuyt=vbnm876dfgh"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizza_resturant.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False
migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
class HomeResource(Resource):
    def get (self):
        response = make_response({"Message":"Pizza Restaurant API."},200)
        return response
        
api.add_resource(HomeResource,"/")

class RestaurantResource(Resource):
    def get (self):
        restaurants = Restaurant.query.all()
        response = make_response(restaurants_schema.dumps(restaurants),200)
        return response
        
        
api.add_resource(RestaurantResource,"/restaurants")



class RestaurantResourceWithId(Resource):
    def get (self, id):
        restaurant_row= Restaurant.query.filter_by(id=id).first()
        if restaurant_row:
            response = make_response(restaurant_with_id_schema.dumps(restaurant_row), 200)
            return response
        else:
            response = make_response({"error" : "Restaurant Not Found!"})
            return response
           
    def delete (self, id):
        restaurant_row= Restaurant.query.filter_by(id=id).first()
        if restaurant_row:
            restaurant_pizzas = RestaurantPizza.query.filter_by(restaurant_id = id).all()
            for rp in restaurant_pizzas:
                db.session.delete(rp)
            db.session.commit()
            db.session.delete(restaurant_row)
            db.session.commit()
            response = make_response({},204)
            return response
        else:
            response = make_response({"error" : "Restaurant Not Found!"},404)
            return response
        
api.add_resource(RestaurantResourceWithId,"/restaurants/<int:id>")

class PizzaResource(Resource):
    def get (self):
        pizzas = Pizza.query.all()
        response = make_response(pizzas_schema.dumps(pizzas),200)
        return response
        
        
api.add_resource(PizzaResource,"/pizzas")

class RestaurantPizzaResource(Resource):
    def post (self):
        try:
            restaurantpizza = RestaurantPizza(
            price = request.get_json()["price"],
            pizza_id = request.get_json()["pizza_id"],
            restaurant_id= request.get_json()["restaurant_id"]
            )
            db.session.add(restaurantpizza)
            db.session.commit()
            pizza = Pizza.query.filter_by(id = request.get_json()["pizza_id"]).first()
            response = make_response(pizza_schema.dumps(pizza),200)
            return response
        except ValueError as e:
            response = make_response({  "errors": e.args},400)
            return response
            
            
        
        
api.add_resource(RestaurantPizzaResource,"/restaurant_pizzas")


if __name__ == '__main__':
    app.run(port=5555, debug=True)
    
    