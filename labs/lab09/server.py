from flask import Flask, request
#from number_fun import multiply_by_two, print_message, sum_list_of_numbers, sum_iterable_of_numbers, is_in, index_of_number
import number_fun
from flask_cors import CORS
import config
from json import dumps

app = Flask(__name__)
CORS(app)


@app.route('/multiply', methods=['GET'])
def multiply():
    print('entered this successfully')
    number = request.args.get('number')
    return dumps(number_fun.multiply_by_two(number))

@app.route('/message', methods=['GET'])
def message():
    message = request.args.get('message')
    return dumps(number_fun.print_message(message))

@app.route('/sum', methods=['GET'])
def sum():
    numbers = request.args.getlist('numbers')
    return dumps(number_fun.sum_list_of_numbers(numbers))

@app.route('/iterable', methods=['GET'])
def iterable():
    numbers = request.args.getlist('numbers')
    return dumps(number_fun.sum_iterable_of_numbers(numbers))

@app.route('/search', methods=['GET'])
def search():
    needle = request.args.get('needle')
    haystack = request.args.getlist('haystack')
    return dumps(number_fun.is_in(needle, haystack))

@app.route('/search_idx', methods=['GET'])
def search_idx():
    item = request.args.get('item')
    numbers = request.args.getlist('numbers')
    return dumps(number_fun.index_of_number(item, numbers))

if __name__ == "__main__":
    app.run(port=8080)