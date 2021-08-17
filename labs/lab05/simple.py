from flask import Flask, request

app = Flask(__name__)

# Write your routes here
# Create a name and add to server
@app.route('/name', methods=['POST'])
def add_name():
    #global 
    pass

# Get name from server and output to user
@app.route('/name', methods=['GET'])
def retrieve_name():
    pass

# Remove name from the server
@app.route('/name', methods=['DELETE'])
def remove_name():
    pass

if __name__ == '__main__':
    app.run(port=0)