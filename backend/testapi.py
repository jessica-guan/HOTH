from flask import Flask, request
from flask_restful import Api, Resource, abort, reqparse
from flask_cors import CORS

# init
app = Flask(__name__)
api = Api(app)
CORS(app)

# dict --> use SQL/another storing thing to store database
clothes_list = { 
    1: {'name': 'A', 'type': 'Shirt', 'size': 'S', 'color': 'red', 'brand': 'H&M', 'thrifted': False}, # style
    2: {'name': 'B', 'type': 'Pants', 'size': 'M', 'color': 'pink', 'brand': 'American Eagle', 'thrifted': False},
    3: {'name': 'C', 'type': 'Jacket', 'size': 'L', 'color': 'blue', 'brand': 'Nike', 'thrifted': True},
    4: {'name': 'D', 'type': 'Hat', 'size': 'M', 'color': 'magenta', 'brand': 'Tommy Hilfiger', 'thrifted': True},
    5: {'name': 'E', 'type': 'Socks', 'size': 'XS', 'color': 'black', 'brand': 'UCLA', 'thrifted': False}
}

# create parser object to parse json's
parser = reqparse.RequestParser()

# add arguments (keys/categories in the dictionary)
parser.add_argument('name')
parser.add_argument('type')
parser.add_argument('size')
parser.add_argument('color')
parser.add_argument('brand')
parser.add_argument('thrifted', type = bool)

def abort_if_dne(clothes_id):
    if clothes_id not in clothes_list:
        abort(404, message=f"Clothes {clothes_id} doesn't exist")

class Clothes(Resource): # information about one article of clothing
    def get(self, clothes_id): # get id
        abort_if_dne(clothes_id=clothes_id)
        return clothes_list[clothes_id]
    
    def delete(self, clothes_id): # delete id
        abort_if_dne(clothes_id)
        del clothes_list[clothes_id]
        return '', 204
    
    def put(self, clothes_id): # update info
        args = parser.parse_args()
        if clothes_id not in clothes_list: # if the clothing id is not in the dict, add it (optional)
            clothes_list[clothes_id] = {}
        
        clothes = {'name': args['name'], 'type': args['type'],
                    'size': args['size'], 'color': args['color'], 'brand': args['brand'], 'thrifted': args['thrifted']}
        clothes_list[clothes_id].update(clothes)
        return clothes_list[clothes_id], 201

class ClothesList(Resource): # return information about list of clothes
    def get(self):
        return list(clothes_list.values())
    
    def post(self):
        args = parser.parse_args()
        clothes_id = max(clothes_list.keys()) + 1
        clothes_list[clothes_id] = {'name': args['name'], 'type': args['type'],
                    'size': args['size'], 'color': args['color'], 'brand': args['brand'], 'thrifted': args['thrifted']}
        return clothes_list[clothes_id], 201

api.add_resource(Clothes, '/clothes/<int>clothes_id')
api.add_resource(ClothesList, '/clothes')

if __name__ == '__main__':
    app.run(debug=True)