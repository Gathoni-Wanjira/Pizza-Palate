from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates



db = SQLAlchemy()


class Pizza(db.Model):
    __tablename__ = 'pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime,server_default=db.func.now())
    updated_at = db.Column(db.DateTime,onupdate=db.func.now())
    
    
    restaurants = db.relationship(
        "Restaurant", secondary = "restaurant_pizzas" , back_populates="pizzas"
    ) 

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    
    pizzas = db.relationship(
        "Pizza", secondary = "restaurant_pizzas" , back_populates = "restaurants"    
    )

    
class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer , db.ForeignKey("pizzas.id"))
    restaurant_id = db.Column(db.Integer , db.ForeignKey("restaurants.id"))
    price = db.Column(db.Integer ,  db.CheckConstraint(
            "price >=1 AND price <=30", name="Price value is not within range 1 and 30"
        ))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    @validates("price")
    def validate_price(self, key, price):
        if not(price >= 1 and price <=30):
            raise ValueError("The price is not in the acceptable range!")
        return price
            
    