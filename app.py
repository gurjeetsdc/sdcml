# import the Flask class from the flask module
from sdcPredictor import SdcPredictor
from flask import Flask, render_template, request

# create the application object
app = Flask(__name__)

sp = SdcPredictor()

# use decorators to link the function to a url
@app.route('/')
def home():	
	return render_template('welcome.html')  # render a template

@app.route('/welcome')
def welcome():

    return render_template('welcome.html')  # render a template

@app.route('/process', methods=['post'])
def process():
	exp = request.form.get("exp")
	result = sp.predict(exp)
	return '<h2>Estimated Salary is calculated as: %.2f</h2>' %(result[0])

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)