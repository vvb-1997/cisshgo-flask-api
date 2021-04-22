from flask import Flask, jsonify, request
from werkzeug.routing import PathConverter
from connect import SSHConnector

# creating a Flask app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

class InterfaceConverter(PathConverter):
    regex = '.*?'

app.url_map.converters['int_'] = InterfaceConverter

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})
  
@app.route('/api/', methods = ['GET'])
def display_all():
    interfaces = SSHConnector()
    return jsonify({'data': interfaces})

@app.route('/api/<int_:interface>', methods = ['GET'])
def display_one(interface):
    interface = SSHConnector(interface)
    return jsonify({'data': interface})
  
# driver function
if __name__ == '__main__':
    app.run(debug = True)