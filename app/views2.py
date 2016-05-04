from flask import Flask
from flask import render_template
from flask import request, redirect
from flask import json, jsonify

from flask import make_response

app = Flask(__name__)
global email

#renders the main website using the index template.html template
@app.route('/')
def hello_world():
    return render_template('index.html')

#using a post method to sign up
@app.route('/signup', methods = ['POST'])
def signup():
	email = request.form['email']
	print("most recent email address is '" + email + "'")
	return redirect('/')

#Making the JSON with fake data.
@app.route('/JSON')
def dispJSON():
	varlist = {'email': 'fake-email@example.com'}
	methodlist={'signup': 'type: POST', 
				'hello_world':'request_type:____',
				'dispJSON': 'request_type:____'}
	return jsonify(Variables=varlist, methods=methodlist)

if __name__ == '__main__':
	app.run(debug=True)
