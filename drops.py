"""
El siguiente programa contrulle una onomatopeya escrita del sonido de gotas (de agua tal vez) en funcion al factor o modulo de un numero dado.
se creo una funcion que recibe como aprametro un numero. En esta funcion primero se valida que el numero introducido sea un entero, si no lo es o es otro tipo de dato,
la funcion imprime un mensaje de error y se sale del programa.

Si la validacion pasa entonces se crea una variable para cada sonido. y una variable final con el resultado de todas las cncatenaciones de los sonidos.
El requermineto indica que si el factor del numero dado es 3 la respuesta del programa debe ser Plic, si el factor es 5 Plac y si es 7 Ploc.
Para determinar esto utilizamos la operacion modulo (%) de python y hacemos: Si el modulo o resto de la division entre el numero dado y 3 es 0 significa ca 3 es factor del numero.
Lo mismo lo aplicamos apra 5 y 7. cada vez que una valdiacion se cumple, escribimos el sonido en la variable final y vamos concatenando todos los resultados validos.
Si ocurre el nuemro dado no es factor de 3 de 5 o de 7, simplemente imprimimos una representacion string del entero suministrado.

"""

import sys

def num_to_drops(num): #creamos la funcion para convertir el numero de entrada en sonidos de gotas.
	if type(num)!= int: #primero validamos que lo ingresdo sea un numero entero
		print("Error: El parametro ingresado no es un numero entero") #si no lo es, devolvemos un error y salimos del programa
		sys.exit() #salimos del programa.
	else: #si el numero es un entero creamos las tres variables que almacenaran las onomatopeyas de los sonidos de las gotas y la variable donde iremos escribeindo los sonidos.
		Plic = "Plic"
		Plac = "Plac"
		Ploc = "Ploc"
		result = ""
		if num%3 == 0: # si el resto (o modulo) de num/3 es 0 quiere decir que 3 es factor de num por lo que asignamos Plic al string final (result)
			result += Plic
		if num%5 == 0: # si el resto (o modulo) de num/5 es 0 quiere decir que 5 es factor de num por lo que asignamos Plac al string final (result)
			result += Plac
		if num%7 == 0: # si el resto (o modulo) de num/7 es 0 quiere decir que 7 es factor de num por lo que asignamos Ploc al string final (result)
			result += Ploc
		if result == "":
			result = str(num) #si no se cumple ninguna de las condiciones anteriores el string 'result' estara vacio. Esto quiere decir que el numero ingresado no tiene 3, 5 o 7 como factores, por lo que regresamos una representacion en string del numero ingresado. 
		return result

if __name__ == "__main__":
        print(f" Numero = 130\n {num_to_drops(130)}")
        print("\n")
        print(f" Numero = 28\n {num_to_drops(28)}")
        print("\n")
        print(f" Numero = 100\n {num_to_drops(100)}")
        print("\n")
        print(f" Numero = 30\n {num_to_drops(30)}")
        print("\n")
        print(f" Numero = 68\n {num_to_drops(68)}")
        print("\n")

        sys.exit()
