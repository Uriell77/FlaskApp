
class usuario():

	def __init__(self, nombre, apellido, correo, password, confirmacion):
		self.nombre = nombre
		self.apellido = apellido
		self.correo = correo
		self.passwword = password
		self.confirmacion = confirmacion

	def booleano(self):
		if self.passwword != self.confirmacion:
			return False
		else:
			return True

