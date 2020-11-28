"""
para este ejercicio se crea una una clase que sirve de contenedor de metodos. los metodos declarados en ella son estaticos, por lo que pueden accederse
sin instanciar la clase.
para cumplir connel requermiento solicitado, se ceo un metodo para cda solicitud: Un metodo que obtiene al mayor valor de puntaje, otro para el ultimo valor ingresado y otro para
el resumen de los 3 mayores resultados.

El problema se modelo utilizando una lista puesto que esta nor permite realizar todas estas funciones de manera directa.
Para el caso del valor mas alto, creamos el metodo 'mas_alto' el cual toma como argumento una lista (que contiene las puntuaciones a evaluar) y la ordena de mayor
a menos con el metodo sort(). Hecho esto, retorna el resultadodelprimero valor, que seria el mas alto de la lista.

para obtener el ultimo valor agregado simplemtne pasamos la lista tal cual se suministra y le suministramos un indice negativo, en este caso -1, con la cual otendramos
el ultimo valor de la lista. original, lo cual conide con el ultimo elemente agregado a ella.

Para obtener los 3 registros mas altos, realizamos un slicing de la lista luego de ordenarla demanera decreciente. Con esto devolvemos una sublista que contiene los 3 registros mas altos en la lista.
Primero debemos comrpobar q la lista contenga el menos 3 elementos. Si no es asi, se imprime un mensaje de error.
"""

class Scores(object):

    def mas_alto(lista):
        lista_ordenada = lista.copy()
        lista_ordenada.sort(reverse=True)
        return lista_ordenada[0]

    def ultimo_agregado(lista):
        return lista[-1]

    def primeros_tres(lista):
        if len(lista) < 3:
            return "ERROR!. La lista es demasiado corta! para obtener 3 valores!"
        else:
            lista_ordenada = lista.copy()
            lista_ordenada.sort(reverse=True)
            return lista_ordenada[0:3]

if __name__ == "__main__":

    lista_1 = [20, 30, 8, 45, 9, 8]
    print(f"La primera lista es {lista_1}")
    print(f"-El valor mas alto es {Scores.mas_alto(lista_1)}")
    print(f"-El ultimo valor ingresado es {Scores.ultimo_agregado(lista_1)}")
    print(f"-Los tres valores mas altos son: {Scores.primeros_tres(lista_1)}")
    print("\n\n")
    lista_2 = [2, 41, 83, 41, 92, 8]
    print(f"La segunda lista es {lista_2}")
    print(f"-El valor mas alto es {Scores.mas_alto(lista_2)}")
    print(f"-El ultimo valor ingresado es {Scores.ultimo_agregado(lista_2)}")
    print(f"-Los tres valores mas altos son: {Scores.primeros_tres(lista_2)}")
    print("\n\n")
    lista_3 = [1, 15]
    print(f"La tercera lista es {lista_3}")
    print(f"-El valor mas alto es {Scores.mas_alto(lista_3)}")
    print(f"-El ultimo valor ingresado es {Scores.ultimo_agregado(lista_3)}")
    print(f"-Los tres valores mas altos son: {Scores.primeros_tres(lista_3)}")

    
