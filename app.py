# import the Flask class from the flask module
from flask import Flask, render_template, request

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/process', methods=['post'])
def process():
	first_name = request.form.get("exp")

	return 'Processing data. '+ str(first_name)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)