from app import app
from flask import render_template, jsonify


@app.route('/', methods= ['GET', 'POST'])

def homepage():
	return render_template('homepage.html')

@app.route('/results') 

def results():
	my_results = {"calories": 550,
					"fat cal": 110,
					"fat GM": 5,
					"fat %": 20,
					"sat fat GM": 9999,
					"sat fat %": 21,
					'trans fat GM': 0,
					"Chol MG": 0,
					"Chol %": 0,
					"sodium MG": 2,
					"sodium %": 3,
					"carbs GM": 77,
					"carbs %": 3333,
					"Dietary fiber GM": 6,
					"Dietary fiber %": 7,
					"sugars GM": 999,
					"protien GM": 9900990,
					"calcium %":10,
					"iron %": 20
					}
	if(request.method == 'GET'):
		return jsonify(my_results)
	if(request.method == 'POST'):
		return "Nothing to post to yet"

