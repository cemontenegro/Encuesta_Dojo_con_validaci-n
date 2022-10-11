from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo_model import Dojo

# nuestra ruta de índice manejará la representación de nuestro formulario
@app.route('/')
def index():
	return render_template("index.html")


@app.route('/crear/dojo',methods=['POST'])
def crear_dojo():
	session['nombre'] = request.form['nombre']
	session['ubicacion'] = request.form['ubicacion']
	session['idioma'] = request.form['idioma']
	session['comentario'] = request.form['comentario']

	if Dojo.is_valid(request.form):
		Dojo.save(request.form)
		return redirect('/results')
	return redirect('/')

@app.route('/results')
def results():
	return render_template('result.html', dojo = Dojo.get_last_dojo())
