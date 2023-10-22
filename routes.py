from flask import Blueprint, jsonify, request
#from __init__ import collection

main = Blueprint('main', __name__)
@main.route('/', methods=['GET'])
def default():
    try:
        if request.method == "GET":
            print('Received GET Request')
            return "Hello Backend", 201
    except Exception as e:
        print(f"Error : {e}")
    return "Can't add", 404

@main.route('/add_item', methods=['POST'])
def add_item():
    try:
        if request.method == "POST":
            print('Received POST Request')
            return jsonify({"name": "Tong Jing Yen", "course": "Computer Engineering", "year": "2023", "cca": "RHDevs, Commotion, Voices"}), 201
    except Exception as e:
        print(f"Error : {e}")
    return "Can't add", 404