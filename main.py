from flask import Flask, jsonify, request, render_template
from werkzeug.routing import PathConverter
from connect import SSHConnector
from forms import InputForm
import json

# creating a Flask app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = 'VeryHardToGuessKey'

class InterfaceConverter(PathConverter):
    regex = '.*?'

app.url_map.converters['int_'] = InterfaceConverter

# on the terminal type: curl http://127.0.0.1:5000/
@app.route('/', methods=['GET', 'POST'])
def home():
    form = InputForm()
    if form.validate_on_submit():
        interface = form.Interface.data
        print(interface)
        data = display_one(interface).get_json()["data"]
        print(data)
        return render_template('home.html', form=form, title="Home page", data=data)   
    return render_template('home.html', form=form, title="Home page")    
  
@app.route('/api/', methods = ['GET'])
def display_all():
    interfaces = SSHConnector()
    return jsonify({'data': interfaces})

@app.route('/api/<int_:interface>', methods = ['GET'])
def display_one(interface):
    data = SSHConnector(interface)
    return jsonify({'data': data})
  
# driver function
if __name__ == '__main__':
    app.run(debug = True)