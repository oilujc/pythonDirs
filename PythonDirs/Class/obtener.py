import os, sys
from os import listdir
from os.path import isfile, join
from .validaciones import Validaciones
from .objetos import Objetos

class Obtener():

	def __init__(self):
		self.arch = []

	def subMenuArchivos(self):
		print("+---------------OPCIONES---------------+")
		print("+  1) BUSCAR PALABRA EN (ARCHIVOS) TXT +")
		print("+  2) BUSCAR PALABRA EN (ARCHIVO) TXT  +")
		print("+  3) CAMBIAR DIRECTORIO               +")
		print("+  4) VOLVER                           +")
		print("+--------------------------------------+")
		opc = int(input('SELECCIONA UNA OPCION: '))
		return opc

	def subMenuArchivosAcciones(self):
		print("+---------------OPCIONES---------------+")
		print("+  1) LEER ARCHIVO                     +")
		print("+  2) VOLVER                           +")
		print("+--------------------------------------+")
		opc = int(input('SELECCIONA UNA OPCION: '))
		return opc

	def subMenuArchivosAccionesHijo(self):
		print("+---------------OPCIONES---------------+")
		print("+  1) BUSCAR PALABRA EN ESTE ARCHIVO   +")
		print("+  2) VOLVER                           +")
		print("+--------------------------------------+")
		opc = int(input('SELECCIONA UNA OPCION: '))
		return opc

	def dirs(self, ruta = '.'):	
		arch = listdir(ruta)

		act = False
		while act != True:
			os.system('cls')
			self.mostrarArchivos(arch)
			opc = self.subMenuArchivos()

			if opc == 1:
				self.buscarPalabraMultiplesArchivosTxt(ruta, arch)
			elif opc == 2:
				self.seleccionarArchivo(ruta, arch)
			elif opc == 3:
				self.cambiarDirectorio(ruta, arch)
			elif opc == 4:
				act = True
			else:
				print("Debes seleccionar una opcion valida")
				input('Continuar...')

	def buscarPalabraMultiplesArchivosTxt(self,ruta,arch):
		dicc = {}
		lista = {}
		act = False
		self.buscar_y_mostrar(arch,ruta,dicc,lista)

		while act != True:
			opc = self.subMenuArchivosAcciones()
			if opc == 1:
				self.seleccionarArchivo(ruta, arch)
			elif opc == 2:
				act = True
			else:
				print("Debes seleccionar una opcion valida")
				input('Continuar...')

		else:
			print("No hay archivos donde buscar")
			input('Continuar...')	

		input('Continuar...')


	def seleccionarArchivo(self,ruta, concat):
		os.system("cls")
		print("+----------SELECCIONAR ARCHIVO--------+")
		self.mostrarArchivos(concat)
		opc = int(input("Seleccione un archivo de la lista: "))
		dire = Validaciones.validacionRutaConcat(ruta, concat[opc])
		self.abrirArchivo(dire,concat[opc])

	def abrirArchivo(self,arch,concat):
		act = False
		dicc = {}
		lista = {}
		for lineas in open(arch):
			print(lineas)

		while act != True:
			opc = self.subMenuArchivosAccionesHijo()
			if opc == 1:
				self.buscar_y_mostrar_archivo_especifico(arch,concat,dicc,lista)
				act = True
			elif opc == 2:
				act = True
			else:
				print("Debes seleccionar una opcion valida")
				input('Continuar...')
		input('Continuar...')

	def buscar_y_mostrar_archivo_especifico(self,ruta,concat,dicc,lista):
		contlineas = 0	
		palabra = Validaciones.stringValidator()
		archivo = open(ruta,'r')
		dicc[concat] = Objetos()
		for lineas in archivo:
			contlineas+=1
			
			if palabra in lineas.lower():
				lineasConcat = "Linea: " + str(contlineas) + " || " + lineas
				dicc[concat].agregarObjetos(lineasConcat)

		archivo.close()
		
		for archivo, linea in dicc.items():
			if len(linea.retornarObjetos()) > 0:
				print("%s"%(archivo))
				for texto in linea.retornarObjetos():
					print("%s"%(texto))


	def buscar_y_mostrar(self,arch,ruta,dicc,lista):
		archVal = Validaciones.validacionArchivos(arch)
		if archVal:

			palabra = Validaciones.stringValidator()
			for archi in arch:
				contlineas = 0
				print("Leyendo archivo: %s"%(archi))
				archConcat = ruta+"\\"+archi
				archivo = open(archConcat,'r')
				dicc[archi] = Objetos()
				for lineas in archivo:
					contlineas+=1
					if palabra in lineas.lower():
						lineasConcat = "Linea: " + str(contlineas) + " || " + lineas
						dicc[archi].agregarObjetos(lineasConcat)
						
				archivo.close()
				
				
				
			for archivo, linea in dicc.items():
				if len(linea.retornarObjetos()) > 0:
					print("%s"%(archivo))
					for texto in linea.retornarObjetos():
						print("%s"%(texto))


	def cambiarDirectorio(self, ruta, concat):
		print("+-----CAMBIAR DIRECTORIO----------+")
		opc = int(input("Seleccione un directorio de la lista: "))
		dire = Validaciones.validacionRutaConcat(ruta, concat[opc])
		self.dirs(dire)

	def mostrarArchivos(self, arch):
		cont = 0
		print("+--------ARCHIVOS----------+")
		for archi in arch:
			cont += 1
			dire = Validaciones.docValidator(archi)
			if dire:
				cadena = "(Archivo)"
			else:
				cadena = "(Directorio)"
			print("%i) %s || %s"%((cont - 1), archi, cadena))

