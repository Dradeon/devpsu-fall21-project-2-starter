from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json

# Use this file as the flask app source if selected
app = Flask(__name__)

# enable CORS
CORS(app)

TO_DO_LIST = [
    {
        'name': 'DevPSU Project 1',
        'description': 'Github Project',
        'deadline': '10-19-2021',
        'completed': False,
    },
    {
        'name': 'DevPSU Project 2',
        'description': 'Vue Frontend Project',
        'deadline': '11-9-2021',
        'completed': False,
    },
    {
        'name': 'CMPSC Final',
        'description': 'Study a lot for final',
        'deadline': '12-15-2021',
        'completed': False,
    }
]

JOURNAL_CONTENT = "Hello there! Begin typing anything in this journal! (It's also resizeable!)"

# Handle Routing for the app
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_name(name=None):
    return render_template('hello.html', name=name)

@app.route('/parks')
def read_users():

    # Read the parks.json file and store it as parks
    with open('parks.json', 'r') as f:
        parks = json.load(f)

    return render_template('parks.html', parks=parks)

@app.route('/todolist', methods=['GET', 'POST'])
def index():

    response_dict = {
        'status': 'success',
        'message': '',
        'to_do_list': TO_DO_LIST
    }

    if request.method == 'POST':
        # update the to do list
        TO_DO_LIST.clear()
        TO_DO_LIST.extend(request.get_json())
        response_dict['message'] = 'List updated'
    else:
        # return default list
        response_dict['message'] = 'List acquired'

    return jsonify(response_dict)

@app.route('/journal', methods = ['GET','POST'])
def journal_func():
    global JOURNAL_CONTENT
    response_dict = {
        'status': 'success',
        'message': '',
        'journal_content': JOURNAL_CONTENT
    }

    if request.method == 'POST':
        JOURNAL_CONTENT = request.get_json()[0]
        response_dict['message'] = 'Contents updated'
    else:
        response_dict['message'] = 'Contents acquired'
    
    return jsonify(response_dict)

# If this file is executed, run the app
if __name__ == "__main__":
    app.run()
