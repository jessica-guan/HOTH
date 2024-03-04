# for backend server stuff
from flask import Flask, request
from flask_restful import Api, Resource, abort, reqparse
from flask_cors import CORS

# for username/password for locally hosted mysql
from config import DATABASE_CONFIG

# mysql connector
import mysql.connector

# getting password for MySQL access
username = DATABASE_CONFIG['username']
password = DATABASE_CONFIG['password']

# connecting to database
database = mysql.connector.connect(
    host="localhost",
    user=username,
    password=password,
    database="hothclothes"
)

# create cursor to retrieve data from database
cursor = database.cursor()

# select all rows from table named "Clothes"
table_name = "Clothes"
cursor.execute(f"SELECT * FROM {table_name}")

result = cursor.fetchall()

clothes_list = {}
# Iterate through the result and print each row
for row in result:
    key = row[0]

    value_dict = {
        'name': row[1],
        'type': row[2],
        'size': row[3],
        'color': row[4],
        'thrifted': row[5],
        'image_url': row[6]
    }

    clothes_list[key] = value_dict


# init
app = Flask(__name__)
api = Api(app)
CORS(app)

# create parser object to parse json's
parser = reqparse.RequestParser()

# add arguments (keys/categories in the dictionary)
parser.add_argument('name')
parser.add_argument('type')
parser.add_argument('size')
parser.add_argument('color')
parser.add_argument('thrifted')
parser.add_argument('image_url')

def abort_if_dne(clothes_id):
    if clothes_id not in clothes_list:
        abort(404, message=f"Clothes {clothes_id} doesn't exist")

class Clothes(Resource): # information about one article of clothing
    def get(self, clothes_id): # get id
        abort_if_dne(clothes_id=clothes_id)
        return clothes_list[clothes_id]
    
    def delete(self, clothes_id): # delete id
        abort_if_dne(clothes_id)
        query = "DELETE FROM Clothes WHERE id = %s"
        data = (clothes_id,)

        cursor.execute(query, data)
        database.commit()

        del clothes_list[clothes_id]
        return '', 204
    
    def put(self, clothes_id): # update info
        args = parser.parse_args()
        abort_if_dne(clothes_id)
        
        # Logging the PUT request data
        print("Received PUT request data for clothes_id:", clothes_id)
        print("Updated data:", args)

        query = """
        UPDATE Clothes
        SET name = %s, type = %s, size = %s, color = %s, thrifted = %s, image_url = %s
        WHERE id = %s
        """
        data = (args['name'], args['type'], args['size'], args['color'], args['thrifted'], args['image_url'], clothes_id)

        cursor.execute(query, data)
        database.commit()

        return args, 201

class ClothesList(Resource): # return information about list of clothes
    def get(self):
        cursor.execute(f"SELECT * FROM {table_name}")
        result = cursor.fetchall()

        clothes_list = []
        for row in result:
            value_dict = {
                'name': row[1],
                'type': row[2],
                'size': row[3],
                'color': row[4],
                'thrifted': row[5],
                'image_url': row[6]
            }

            clothes_list.append(value_dict)

        return clothes_list
    
    def post(self):
        args = parser.parse_args()
        print("Received POST REQUEST")

        print(args)
        query = """
        INSERT INTO Clothes (name, type, size, color, thrifted, image_url)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        data = (args['name'], args['type'], args['size'], args['color'], args['thrifted'], args['image_url'])

        cursor.execute(query, data)
        database.commit()

        new_id = cursor.lastrowid

        return args, 201

api.add_resource(Clothes, '/clothes/<int>clothes_id')
api.add_resource(ClothesList, '/clothes')

if __name__ == '__main__':
    app.run(debug=True)