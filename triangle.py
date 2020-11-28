"""
El sigueinte codigo calcula el area de un triangulo valiendose de los valores de los 3 lados del mismo.
Para lograrlo Se crea una clase dentro del programa llamada triangulo que implementa los metodos necerios para identificar que tipo de triangulo es el triangulo
suministrado y con esta informacion calcular su area.
El area de un triangulo es (1/2)*(b*h) o Un medio de la base por la altura, donde b es la base de triangulo y h es su altura. Sin embargo no todos los
triangulos son iguales y existen varias maneras de clasificarlos. Dadas las condiciones de nuestro problema, en el cual solo se nos suministran las longitudes
de los lados del triangulo, debemos obtar por la clasificacion basada en este aspecto. De este modo, los triangulos se dividen en:
Equilateros, Isosceles, Escaleno
y Rectangulo. esto es improtante porque dependiendo del tipo de triangulo hay una formula para el calculo de su altura, y por consiguiente par ala determinacion de su area.

            -Triangulo Equilatero: tirangulo que tiene todos sus lados iguales (__a = __b = __c)
            -Triangulo Isósceles: Trinagulo en el que al menos 2 de sus lados son iguales. (__a =__b | __a = __c | __b = __c)
            -Triangulo Escaleno: Triangulo en el que ninguno de sus lados es igual a otro. (__a != __b != __c)\
            -Triangulo Rectangulo: Triangulo en el que al menos uno de sus angulos es de 90 grados. Adicionalmente, se cumple que uno de los lados es la raiz cuadrada
            de la suma de los cuadrados de los otros 2 lados.

Para que el programa fuese capaz de determinar que triangulo esta calculando, se realizaron una serie de comprobaciones en los datos suministrados al mismo (los lados del
triangulo) para clasificarlo y aplicarle la formula correspondiente.Estas comprobaciones son:

- Primero se crea una lista ordenada de mayor a menor con los valores de los 3 lados del triangulo. Esto permite establecer criterios comparativos entre los lado ya que
por ejemplo, los valores mas altos siempre van a ubicarse en la primera posicion de la lista y los mas bajos al final.
-Armados con la lista procedemos a comparar el primer valor con el segundo. Si estos son iguales, procedemos a compararlos con el tercer. Si los 3 son iguales
estamos en presencia de un trinagulo equilatero por lo que llamados al metodo que calcula el area para este tipo de triangulo, pasandole como parametro el valor de alguno de los lados.
-Si ocurre que el primer valor y el segundo son iguales, pero no ocurre lo mismo con el tercero, entonces quiere decir que el triangulo es Isosceles por lo que llamamos
al metodo que calcula el area para este tipo de triangulo.
-Si al comparar el priemr valor y el segundo, encontramos que no son iguales,comparamos el segundo valor con el tercero.
-Si resultan ser iguales, estamos nuevmanteen prsencia de un triangulo isosceles.Pero si resulta que tampoco son iguales, etonces el trinagulo es Escaleno o
Rectangulo.Un trinagulo rectangulo se identifica porque generalemtne solo se suministran 2 de sus lados, en nuestro caso el problema indica que se suminsitran
3 lados, por lo que entonces, uno de ellos debe ser la hipotenuza del triangulo. La hipotenusa es la parte o el lado de mayor longitud en un triangulo rectangulo
porque representa la raiz cuadrada de la suma de los cuadrados de sus otros lados, por lo que directamente podemos afirmar que hipoteticamente, el primer valor de
nuestra lista ordenada es la hipotenusa del trinagulo. De modo que los otros 2 valores serian sus lados (o catetos).
Armados cone sta premisa se creo un metodo que otiene la hipotenuza del triangulo dado y lo compara con el valor mas alto de la lista ordenada. Si coninciden,
quiere decir que el triangulo es rectangulo por lo que se llama al metodo que calcula su area.
-Si el triangulo no es rectangulo, entonces, es escaleno y se llama el metodo que calcula el area para este tipo de triangulo.

Todos los metodo retornan un valor numerico que luego puede ser impreso por pantalla o almacenado en alguna variable

"""


class Triangulo(object): #definimos la clase que va a servir de marco para nuestros objetos.
            def __init__(self): #definimos el constructor de la clase y en definimos los 3 lados del triangulo como stributos "privados" 
                    self.__a = None
                    self.__b = None
                    self.__c = None
                    pass
            #definimos 3 metodos publicos, uno para cargar cada uno de los lados del triangulo. redondeamos el valor ingresado a un solo decimal
            def set_lado_a(self, valor):
                    self.__a = round(valor,2)
                    pass
            def set_lado_b(self, valor):
                    self.__b = round(valor,2)
                    pass
            def set_lado_c(self, valor):
                    self.__c = round(valor,2)
                    pass

            """Un triangulo es una figura goemetrica de tres lados, sin embargo, en funcion a las proporciones de sus lados un triangulo puede clasificarse en 4 tipos:
            
            Para identificar que tipo de triangulo esa calculando el programo hacemos una serie de comprobaciones para poder clasificar el triangulo segun la longitud
            de sus lados y asi poder aplicar la formula del area segun el caso que corresponda.
            """
            
            def __isosceles(self, lado_a, lado_b): #definimos la funcion para calcular el area de un triangulo isosceles. Se toman solo 2 lados ya que se supone que el tercero es igual a algun otro
                    area = (lado_b*(lado_a**2 - ((lado_b**2)/4))**0.5)/2 # aplicamos la formula del area para este tipo de triangulo
                    return area # devolvemos el valor a la funcion que realizo la invoacion.

            def __equilatero(self, lado_a):#definimos la funcion para calcular el area de un triangulo Equilatero. Se toma solo 1 lado ya que se suponen iguales entre si.
                    area = ((3**0.5)/4)*(lado_a**2)# aplicamos la formula del area para este tipo de triangulo
                    return area# devolvemos el valor a la funcion que realizo la invoacion.

            def __escaleno(self, lado_a, lado_b, lado_c):#definimos la funcion para calcular el area de un triangulo escaleno. Se toman los 3 lados porque son diferentes entre si
                    s = (lado_a + lado_b + lado_c)/ 2# calculamos el semiperimetro del triangulo, ya que este valor lo necesitaremos para poder hallar la altura
                    area = (s*(s-lado_a)*(s-lado_b)*(s-lado_c))**0.5 # aplicamos la formula del area para este tipo de triangulo
                    return area# devolvemos el valor a la funcion que realizo la invoacion.

            def __rectangulo(self, lado_a, lado_b):#Definimos la funcion para el triangulo rectangulo, para el cual solo se toman 2 lados ya que el tercero representa a la hipotenusa.
                    area = (lado_a * lado_b)/2
                    return area

            #esta funcion determina si el triangulo ingresado es rectangulo. para ello debe cumplirse que uno de los lados sea la raiz cuadrada de la suma de los cuadrados de los
            #otros 2. Si esto se cumple podemos afirmar que el triangulo es rectangulo.
            def __is_rectangulo(self, lados):
                    hipotenusa = ((lados[1]**2) + ((lados[2])**2))**0.5 # calculamos la hipotenusa del trinagulo suministrado
                    hipotenusa = hipotenusa
                    if round(hipotenusa,1) == round(lados[0],1):# verificamos que la hipotenusa sea igual al lado mas largo del triangulo suministrado. aplicamos la funcion de redondeo a un decimal para standarizar los numeros a comparar
                            return True # si lo es, retornamos True validando que se trata de un triangulo rectangulo
                    else:
                            return False #si no se cumple, regresamos False

                        
            #aqui definimos el metodo principal, el cual se encarga de calcular el area de un triangulo en funcion de su tipo.
            # El area de un triangulo es la un medio del producto de su base por su altura. Sin embargo, hay disntintas formas de calcular la altura de un triangulo dependiendo
            # de su tipo o de los valores iniciales que se posean. En nuestro caso, nos basaremos en los tipos de tirnagulo en funcion a las rerlaciones entre sus lados.
            def get_area(self): 
                    self.__lados = [self.__a, self.__b, self.__c] # lo rpimero que hacemos es es definir una lista privada donde almacenaremos los lados ingresados
                    self.__lados.sort(reverse=True) # ordenamos la lista de mayor a menos. Esto es para poder tener los datos en una forma que nos permita trabajarlos mejor y hacer
                    #algunos supuestos sobre ellos. Por ejeplo, el primer dato siempre sera el lado mas largo, por lo tanto el calculo de la hipotenusa se realiza
                    #en base a el. Asi mismo, si hay lados iguales, uno de ellos es el valor central y el otro esta en alguno de los extremos.

                    if self.__lados[0] == self.__lados[1]:# primero comprobamos si el lado mas largo y el segundo lado mas largo son iguales. Si lo son
                            if self.__lados[1] == self.__lados[2]:#comparamos si el segundo es igual al tercero. Si se cumple el triangulo es equilatero y retornamos el resultado del metodo privado __equilatero.
                                    return self.__equilatero(self.__lados[0]) #pasando como parametro uno de los lados ya que todos son iguales.
                            else: # si por el contrario el segundo lado y el tercero son distintos, sabiendo que el priemro y el segundo son iguales, podemos afirmar que el tirangulo es isosceles.
                                    return self.__isosceles(self.__lados[0], self.__lados[2]) #retornamos el resultado del metodo__isosceles pasando como parametro uno de los lados iguales y el lado diferente
                    else:# si el lado mas largo y el segundo mas largo NO son iguales pueden ocurrir 2 cosas, que la igualdad este en los otros 2 lados, o que los 3 lados sean distintos entre si.
                            if self.__lados[1] == self.__lados[2]: # lo primero que hacemos es verificar si el segundo mas largo y el tercero son iguales. Si se cumple
                                    return self.__isosceles(self.__lados[1], self.__lados[0]) # nuevamente estamos en presencia de un tirnagulo Isosceles, sabiendo que el primero lado es el diferente
                            else: # si la igualdad tampoco esta en los ultimos 2 lados entonces el triangulo es rectangulo o es escaleno. Para determinarlo consultamos el
                                    if self.__is_rectangulo(self.__lados):#el resultado del metodo __is_rectangulo pasandole como parametro una lista con el arreglo ordenado de lados que ya teniamos
                                            self.__lados.pop(0)# si el metodo devuelve True, borramos el lado mas largo de la lista (que seria la hipotenusa) y llamamos al metodo __rectangulo con los 2 lados restantes.
                                            return self.__rectangulo(self.__lados[0], self.__lados[1])
                                    else: # si el metodo no retorna True, quiere decir que el triangulo es escaleno, asi que llamamos a este metodo pasandole como argumentos los 3 lados suministrados al objeto de la clase Triangulo
                                            return self.__escaleno(self.__lados[0], self.__lados[1], self.__lados[2])

if __name__ == "__main__":
    equilatero = Triangulo()
    equilatero.set_lado_a(5)
    equilatero.set_lado_b(5)
    equilatero.set_lado_c(5)
    print(f" Lados 5, 5, 5\n El area del triangulo es {equilatero.get_area()}\n Este triangulo es Equilatero. Todos sus lados son iguales")
    print("\n\n")
    isosceles = Triangulo()
    isosceles.set_lado_a(3)
    isosceles.set_lado_b(3)
    isosceles.set_lado_c(2)
    print(f" Lados 3, 3, 2\n El area del triangulo es {isosceles.get_area()}\n Este triangulo es Isósceles. Dos de sus lados son iguales")
    print("\n\n")
    escaleno = Triangulo()
    escaleno.set_lado_a(3)
    escaleno.set_lado_b(2)
    escaleno.set_lado_c(4)
    print(f" Lados 3, 2, 4\n El area del triangulo es {escaleno.get_area()}\n Este triangulo es Escaleno. Todos sus lados son diferentes")
    print("\n\n")
    rectangulo = Triangulo()
    rectangulo.set_lado_a(3)
    rectangulo.set_lado_b(4)
    rectangulo.set_lado_c(5)
    print(f" Lados 3, 4, 5\n El area del triangulo es {rectangulo.get_area()}\n Este triangulo es Rectangulo. Uno de sus aldos es la raiz cuadrado de la suma de los cuadrados de los otros 2 lados")
        
