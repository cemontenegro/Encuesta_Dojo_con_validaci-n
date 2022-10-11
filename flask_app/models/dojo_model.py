from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Dojo:
	def __init__(self,data):
		self.id = data['id']
		self.nombre = data['nombre']
		self.ubicacion = data['ubicacion']
		self.idioma = data['idioma']
		self.comentario = data['comentario']
		self.created_at = data['created_at']
		self.updated_at = data['updated_at']

	@classmethod
	def save(cls,data):
		query = "INSERT into dojos (nombre,ubicacion,idioma,comentario) VALUES (%(nombre)s,%(ubicacion)s,%(idioma)s,%(comentario)s);"
		return connectToMySQL('esquema_encuesta_dojo').query_db(query,data)

	@classmethod
	def get_last_dojo(cls):
		query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
		results = connectToMySQL('esquema_encuesta_dojo').query_db(query)
		return Dojo(results[0])

	@staticmethod
	def is_valid(dojo):
		is_valid = True
		if len(dojo['nombre']) < 5:
			is_valid = False
			flash("Nombre mas de 5 caracteres.")
		if len(dojo['ubicacion']) < 1:
			is_valid = False
			flash("Elegir ubicación de Dojo.")
		if len(dojo['idioma']) < 1:
			is_valid = False
			flash("Elegir lenguaje favorito.")
		if len(dojo['comentario']) < 3:
			is_valid = False
			flash("Comentarios al menos 3 caracteres.")
		return is_valid