from marshmallow import Schema ,fields

class RestaurantSchema(Schema):
    class Meta:
        fields = ("id", "name", "address")


restaurants_schema = RestaurantSchema(many=True)
class PizzaSchema(Schema):
    class Meta:
        fields = ("id", "name", "ingredients")
    

class RestaurantWithIdSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    address = fields.String()
    pizzas = fields.Nested(PizzaSchema , many=True)
    
restaurant_with_id_schema = RestaurantWithIdSchema()
    
   
        