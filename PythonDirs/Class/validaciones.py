from .archivos import Archivos

class Validaciones():
	def __init__(self):
		pass

	@classmethod
	def stringValidator(self):
		cadena = str(input("Ingrese la palabra a buscar: ").lower())
		return cadena

	@classmethod
	def docValidator(self, var):
		cara = 0
		for extensions in Archivos.listado:
			if extensions.lower() in var:
				cara = 1
		return cara

	@classmethod
	def validacionRutaConcat(self,ruta, concat):
		print("Ingrese una ruta valida")
		var = ruta + "\\"+ concat

		if var == "" or var.isspace():
			print("Debes ingresar alguna ruta")
		else:
			return var

	@classmethod
	def validacion(self):
		print("Ingrese una ruta valida")
		ruta = str(input('>>>'))

		if ruta == "" or ruta.isspace():
			print("Debes ingresar alguna ruta")
		else:
			return ruta

	@classmethod
	def validacionArchivos(self, archivo):
		cont = 0
		for arch in archivo:
			for extensions in Archivos.listado:
				if extensions.lower() in arch:
					cont = 1

		return cont

			