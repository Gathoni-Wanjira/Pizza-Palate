from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    
class Pizza(db.Model):
    __tablename__ = 'pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.datetime ,server_default=db.func.now())
    updated_at = db.Column(db.datetime,onupdate=db.func.now())
    
class RestaurantPizza(db.Model):
    __tablename__ = 'restaurants_pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer , db.ForeignKey("pizzas.id"))
    restaurant_id = db.Column(db.Integer , db.ForeignKey("restaurants.id"))
    price = db.Column(db.Integer ,  db.CheckConstraint(
            "price >=1 AND price <=30", name="Price value is not within range 1 and 30"
        ))
    created_at = db.Column(db.datetime, server_default=db.func.now())
    updated_at = db.Column(db.datetime, onupdate=db.func.now())
    
    