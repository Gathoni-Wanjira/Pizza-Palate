from marshmallow import Schema ,fields

class RestaurantSchema(Schema):
    class Meta:
        fields = ("id", "name", "address")


restaurants_schema = RestaurantSchema(many=True)
