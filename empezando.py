print("hola mundo")
#esto es un comentario

suma = 2+2 #esto es una suma
print(suma)
resta = 10-8 #esto es una resta
print(resta)
mult = 5*2 #esto es una multiplicacion
print(mult)
div = 10/2 #esto es una division
print(div)
potencia = 5**3 #esto es una potencia
print(potencia)
residuo = 10%2 #esto es para calcular el residuo o modulo
print(residuo)

#Variables en python so de tipado dinámico
n1 = 8 #Int
n2 = "ocho" #String
n3 = 8.10 #Float
s1 = "esto tambien es un string" #String
b1 = True #Booleano
b2 = False #Booleano

#Saber el tipo de dato de una variable
print ( type(n1) )#Int
print ( type(s1) )#Str
print ( type(b1) )#Bool

#En python todo es un objeto

#Solicitar iformacion
msj = input("ingrese un saludo:")
print (msj)


#if - elif - else 
suscriptor = True

if suscriptor == False:
    print("suscribete")
elif suscriptor == True:
    print("Gracias")
else:
    print("bueno, dale like")

#Operadores de comparacion 
# ==, <, >, <=, =>, != 

#Es muy importante la identacion

#bucles 

#while
x = 0
while x < 8:
    print(x)
    x +=1 #asi con cada vuelta se le agrega uno

#for
for i in range(10):
    print(2**i)

#pytho nos proporciona varios tipos de datos (averiguarlos)

#Lista
lenguajes = ["python", "php", "JavaScript", "C#"]
print(lenguajes)

#Acceder a los elementos
print(lenguajes[0]) #python
print(lenguajes[-1]) #C#

#Agregar un elemento a la lista
lenguajes.append("C++")

#Quitar un elemento de la lista
lenguajes.remove("python")

#Insertar valor en el indice indicado
lenguajes.insert(0,"python")

#contar la cantidad de elementos de la lista con el mismo valor
print(lenguajes.count("python"))

#obtener la longitud de una lista
print(len(lenguajes))

#Retornar y remover un elemento de la lista mediante indice
lang =lenguajes.pop(0)


#Rebanadas, estas no permiten acceder a una porcion de lalista que especifiquemos
lenguajes[1:3]#el ultimo indice no se toma
lenguajes[1:]
lenguajes[:2]


#Concatenacion
print(lenguajes + ["go","Rust"])

#Las listas son mutables, lo que significa que podemos cambiar un valor por otro
lenguajes[-1] = "haskell"
print(lenguajes)

#Listas por comprension
pares = [n for n in range(1,21) if n%2 == 0]
print(pares)

#manera normal de hacer el anterior programa
pares = []
for n in range(1,21):
    if n%2 == 0:
          pares.append(n)
print(pares)

#con str puedo convertir un valor a un string y seria asi
#str(año)

#con int puedo convertir un valor a numeros asi
#int(altura)
#y asi imprimo el valor de una funcion mostrarAltura(y el parametro altura)
#y es importante el return en las funciones


#asi se define una funion
#def mostrar(): #y despues de esto va un if un for o algo asi

"""
esto, no se va a ver, es otra forma de poner comentarios
"""

jugadores = { #esto es un diccionario
    10: "messi",
    7 : "ronaldo"
}
print(jugadores[7])# y asi imprimo un valor de un diccionario

color = "verde"
match color: #este comparador sirve para comparar varios casos
    case "verde":
        print ("correcto")
    case "amarillo":
        print ("vuelve a intentar")
    case _: #asi se capturan situaciones adicionales
        print("error")

#asi se importa un archivo
#import curso python1
#y asi se usa curso python1.multiplicar()
