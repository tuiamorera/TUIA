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

# ****Diccionarios o Matrices
d = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amelie": "Jean-Pierre Jeunet"}
d["Love Actually"]  # devuelve "Richard Curtis"

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
