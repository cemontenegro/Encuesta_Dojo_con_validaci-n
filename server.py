from flask_app import app
from flask_app.controllers import dojos_controller

app.secret_key= 'keep in secret'

if __name__ == "__main__":
	app.run(debug=True)
