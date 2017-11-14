import os, sys
from Class.obtener import Obtener
from Class.validaciones import Validaciones


def menu():
	bienvenida = """BIENVENIDO \nOiluj String Search \nCreado por Julio Martinez\n V 0.0.1
	"""
	print(bienvenida)
	print("+--------MENU----------+")
	print("+  1) BUSCAR ARCHIVOS  +")
	print("+  2) SALIR            +")
	print("+----------------------+")
	opc = int(input('+>>> '))
	return opc


def main():
	hecho = False
	obt = Obtener()
	while hecho != True:

		os.system('cls')
		try:
			opc = menu()

			if opc == 1:
				archi = Validaciones.validacion()
				obt.dirs(archi)
				input('Continuar...')
			elif opc == 2:
				hecho = True
			else:
				print("Opcion Invalida")

		except Exception as e:
			print("ERROR %s"%e)
			input('Continuar...')


	print("Hasta luego")

if __name__ == '__main__':
	main()
