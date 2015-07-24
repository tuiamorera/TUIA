# coding=utf-8
__author__ = 'lmorera'

# ****Variables
c = "cadena"
e = 23
f = 100L
type(c)
type(e)
t = True
f = False

# ****Print
print (c + "larga")
print ""
#Print fecha y hora actual, fecha %d/%m/%y y para la hora %H:%M:%S
import time
print time.strftime("%d/%m/%y %H:%M:%S")
print ""
print("Un tipo le dice a otro: \"¿Cómo estás?\"")
print('Y el otro le contesta: \'¡Pues anda que tú!\'')
print ""

# ****Exponente **
print (2 ** 6)

# ****Sentencia if
if (e > 10): print ("la variable es mayor a 10")
print("fin")

# ****Sentencia if con else
if (e != 23):
    print ("la variable es diferente de 23")
else:
    print("la variable es igual a 23")
print("fin")

#***********************************************************************************************************************
# ****LISTAS o arrays (colecciones)
a = [1, 3, 5]
print(a)

# Acceder a elementos dentro de la lista
primeravariablelista = a[0]
segundavariablelista = a[1]
terceravariablelista = a[2]
print(primeravariablelista)

# Lista dentro de lista
b = [22, True, "una lista", [1, 2]]
mi_var = b[3][0]
print(mi_var)

# Modificar un elemento de una lista
c = [22, True]
c[0] = 99
print(c)
mi_var2 = c[-1]
print (mi_var2)

# Slicing o particionado en listas
l = [99, True, "una lista", [1, 2]]
mi_var3 = l[0:2]
print(mi_var3)
mi_var4 = l[0:4:2]
print (mi_var4)

# ****Tuplas o types
c = "hola todos"
c[0]
print(c[0])
print(c[5:])
print(c[::3])
print(c[3:9])

#***********************************************************************************************************************
# ****Diccionarios o Matrices
d = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amelie": "Jean-Pierre Jeunet"}
d["Love Actually"]  # devuelve "Richard Curtis"

#***********************************************************************************************************************
# ****SENTENCIAS
# If/else
fav = "tuia"
if fav == "tui":
    print("Tienes buen gusto")
    print("Gracias")
else:
    print("no es Tuia")

# if...elif...elif...else
numero = 2
if numero < 0:
    print("negativo")
elif numero > 0:
    print("positivo")
else:
    print("cero")

# En esta construcción se evalúa el predicado C y se devuelve A si se cumple o B si no se cumple: A if C else B.
var = "par" if (numero % 2 == 0) else "impar"
print(var)

# Bucles
# While simple
edad = 0
while edad < 5:
    edad = edad + 1
    print("Felicidades, tienes " + str(edad))

print(" ")
print(" ")

# Continue en un while
edad2 = 0
while edad2 < 18:
    edad2 = edad2 + 1
    if edad2 % 2 == 0:
        continue
    print("Felicidades, tienes " + str(edad2))

#For in
secuencia = ["uno", "dos", "tres"]
for elemento in secuencia:
    print (elemento)

#For usando range (rango) por eje para imprimir los nums del 30 al 50


#Funciones
#Ejemplo1:
def mi_funcion(param1, param2):
    """Esta funcion imprime los dos valores pasados como paramentros"""
    print param1
    print param2

#Testing funciones
mi_funcion("hola", 2)

mi_funcion(param2= 3, param1= "adiós")

#Ejemplo2:
def imprimir (texto, veces= 1):
    print veces * texto

imprimir("UnSoloValor")
imprimir("hola1", 3)

#Definir funcion con un núm variable de argumentos colocar último parametro precedido por asterisco
def variospar(parm1, parm2, *otros):
    for val in otros:
        print val

variospar(1, 2)
variospar(1, 2, 3)
variospar(1, 2, 3, 4, "cinco")

#Utilizando funcion items de los diccionarios devuelve una lista con sus elementos,
#para imprimir los parámetros que contiene el diccionario
def varios(param1, param2, **otros):
    for i in otros.items():
        print i

varios(1, 2, tercero = 3.5)

#Un método no es más que una función que pertenece a un objeto, en este caso a una lista;
#y append, en concreto, sirve para añadir un elemento a una lista.

def funct(a, b):
    a = a+ 3
    b.append(23)
    print a, b

a = 22
b = [22]
funct(a, b)
print a, b

#Como vemos la variable x no conserva los cambios una vez salimos de la función porque los enteros son inmutables en Python.
# Sin embargo la variable y si los conserva, porque las listas son mutables.
# En resumen: los valores mutables se comportan como paso por refe- rencia, y los inmutables como paso por valor.

#Como devolver valores para los que se usa la palabra clave return
def sumar (x, y):
    return x + y
print sumar (3, 2)

def operaciones (f, g):
    return f * 2 + g * 2
print operaciones(1, 2)

#***********************************************************************************************************************
#***Orientación a Objetos

#Un objeto es una entidad que agrupa un estado y una funcionalidad relacionadas.
# El estado del objeto se define a través de variables llamadas atributos,
# mientras que la funcionalidad se modela a través de funciones a las que se les
# conoce con el nombre de métodos del objeto.

#Una clase, por otro lado, no es más que una plantilla genérica a partir￼de la cuál
#instanciar los objetos; plantilla que es la que define qué atri- butos y métodos tendrán los objetos de esa clase.

class Coche:
    "Abstracción de los objetos coche"
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print "Tenemos", gasolina, "litros"

    def arrancar(self):
        if self.gasolina > 0:
            print "Arranca"
        else:
            print "No arranca"

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print "Quedan", self.gasolina, "litros"
        else:
            print "No se mueve"
print ""

#Lo primero que llama la atención en el ejemplo anterior es el nombre tan curioso que tiene el método __init__.
# Este nombre es una convención y no un capricho. El método __init__, con una doble barra baja al principio y
# final del nombre, se ejecuta justo después de crear un nuevo objeto a partir de la clase, proceso que se conoce
# con el nombre de instanciación. El método __init__ sirve, como sugiere su nombre, para realizar cualquier
# proceso de inicialización que sea necesario.
#Como vemos el primer parámetro de __init__ y del resto de métodos de la clase es siempre self.
# Esta es una idea inspirada en Modula-3 y sirve para referirse al objeto actual.
# Este mecanismo es necesario para poder acceder a los atributos y métodos del objeto diferenciando,
# por ejemplo, una variable local mi_var de un atributo del objeto self. mi_var.

#Para crear un objeto se escribiría el nombre de la clase seguido de cual- quier parámetro que sea necesario
# entre paréntesis. Estos parámetros son los que se pasarán al método __init__, que como decíamos es el método
# que se llama al instanciar la clase.
mi_coche = Coche (3)
print mi_coche.gasolina
#Arranca
mi_coche.arrancar()
#Quedan 2 litros
mi_coche.conducir()
#Queda 1 litro
mi_coche.conducir()
#Quedan 0 litros
mi_coche.conducir()
#No se mueve
mi_coche.arrancar()
#No arranca
print mi_coche.gasolina
print ""

#OTROS:
#Uper para devolver texto en mayúsculas
cad= "cadena de caracteres"
print cad.upper()

#count(sub) para devolver número de veces que se encontró la cadena sub en el texto
print cad.count("a")
print ""

#***********************************************************************************************************************
#(encapsulamiento, la herencia (heredar o extender de una clase) y el polimorfismo.)

#HERENCIA

#Para indicar que una clase hereda de otra se coloca el nombre de la cla- se de la que se hereda
# entre paréntesis después del nombre de la clase:
class Instrumento:
    def __init__(self, precio):
        self.precio = precio
    #Método tocar
    def tocar (self):
        print "Estamostocando musica"
     #Método romper
    def romper(self):
        print "Eso lo pagas tu"
        print "Son", self.precio, "$$$"

class Bateria (Instrumento):
    pass

class Guitarra (Instrumento):
    pass
#Como Bateria y Guitarra heredan de Instrumento, ambos tienen un método tocar() y un método romper()

#Se puede sobreescribir métodos: por ejemplo si quisieramos especificar un nuevo parámetro tipo_cuerda a la hora de
#crear un objeto Guitarra. Tendríamos que escribir un nuevo método __init__ para la clase Guitarra
#Eje: Instrumento.__init__(self, precio)

#Herencia múltiple:
#or ejemplo, podríamos tener una clase Cocodrilo que heredara de la clase Terrestre, con métodos como caminar()
# y atributos como velocidad_caminar y de la clase Acuatico, con métodos como nadar() y atributos como velocidad_nadar
class Terrestre:
    def desplazar(self):
        print "El animal anda"

class Acuatico:
    def desplazar(self):
        print "El animal nada"

class Cocodrilo (Terrestre, Acuatico):
    pass
#omo Terrestre se encuentra más a la iz- quierda, sería la definición de desplazar de esta clase la que prevale- cería,
# y por lo tanto si llamamos al método desplazar de un objeto de tipo Cocodrilo lo que se imprimiría sería “El animal anda”.
c = Cocodrilo()
c.desplazar()

#***********************************************************************************************************************
#POLIMORFISMO
47
