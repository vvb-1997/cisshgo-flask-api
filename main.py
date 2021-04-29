from flask import Flask, jsonify, request, render_template
from werkzeug.routing import PathConverter
from flask_restful import Resource, Api
from connect import SSHConnector
# from get_all_interfaces import SSHConnector
from forms import InputForm
import json

# creating a Flask app
app = Flask(__name__)
api = Api(app)
app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = 'VeryHardToGuessKey'

class InterfaceConverter(PathConverter):
    regex = '.*?'

app.url_map.converters['int_'] = InterfaceConverter

# on the terminal type: curl http://127.0.0.1:5000/
@app.route('/', methods=['GET', 'POST'])
def home():
    form = InputForm()
    # data = DisplayAll().get()["data"]
    if form.validate_on_submit():
        interface = form.Interface.data
        data = DisplayOne().get(interface)["data"]
        return render_template('home.html', form=form, title="Home page", data=data)   
    
    return render_template('home.html', form=form, title="Home page")
    # return render_template('home.html', form=form, title="Home page", data=data)    

class DisplayAll(Resource):
    def get(self):
        interfaces = SSHConnector()
        return ({'data': interfaces})

class DisplayOne(Resource):
    def get(self,interface):
        interfaces = SSHConnector(interface)
        return ({'data': interfaces})

api.add_resource(DisplayAll, '/api/')
api.add_resource(DisplayOne, '/api/<int_:interface>/')

# driver function
if __name__ == '__main__':
    app.run(debug = True)