
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

products = {
    'baverage':{'pepsi':{'type': '2ltr bootle', 'price':120, 'qty': 50},
                'coke': {'type': '500 ml bootle', 'price':65, 'qty': 85},
                'sprite':{'type': '300 ml can', 'price': 50, 'qty': 60}},

    'biscuts' :{'marie':{'type': '120 gms pack', 'price': 85, 'qty': 75},
                'goodday':{'type': '50 gms pack', 'price': 30, 'qty': 100},
                'krackjack':{'type': '100 gms pack', 'price': 45, 'qty': 45}}
}

class Products(Resource):
    def get(self, product):
        return {product: products[product]}

api.add_resource(Products, "/getproduct/<product>")

if __name__ == '__main__':
    app.run(debug=True)