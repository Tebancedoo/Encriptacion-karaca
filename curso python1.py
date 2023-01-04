#https://www.youtube.com/watch?v=chPhlsHoEPo
#2:22:22 (curso terminado)
"""Strings"""
#x, book = 100, "i robot"# guardar dos variables a la vez

#myStr = "hola mundo"

#print(f"un saludo pa ti {myStr}")#otra forma de concatenar
#print(dir(myStr))# dir no enseña que podemos hacer con ese tipo de datos (string) en este caso
#el dir nos muestra propiedades y metodos

#print(myStr.upper())
#print(myStr.replace("hola","chao").upper)#replace es para reemplazar
#digo que primero me reemplace el "hola" por "chao" y que despues me ponga todo a mayuscula

#print(myStr.startswith("hola"))#aqui estoy diciendo que quiero saber si mi string comienza con la palabra hola
#startswith sirve para saber si una palabra empieza por lo que yo le diga

#print(myStr.endswith("mundo")) # lo mismo que el anteriror pero al final

#print(myStr.split())# divide my string por los espacios por defecto y me crea una lista

#print(myStr.find("o"))#find busca el parametro (o) en este caso y me devuelve la posicion

#print(len(myStr))#len me devuleve la longitud de un string

#print(myStr.index("n"))#index me devuelve el  indice del parametro que le indique, (n) en este caso

#print(myStr.isnumeric())#me dice si el valo es numerico

#print(myStr.isalpha())#me dice si el valo es alfanumerico

#print(myStr[0])#asi miro la posicion cero de un string

"""Numeros"""

#print(1 + 1) 
#print(2**10)
#print(2%3)#esto devuelve el residuo

"""Listas"""

#numbers_list = list((1,2,3,4))#aqui creo una tupla para que los 4 elementos se me guarden como si fueran 1
#print(numbers_list)

#r = list(range(1,10))#creo una lista con el rango del 1 al 9, por que el ultimo elemento no se cuenta
#print(dir(r))#y con dir me muestra los metodos o lo que puedo hacer con la lista en este caso

#r[1] = "dos"#aqui le digo el el valor que esta en la posicion 1 lo cambie por una palabra que diga (dos)
#print(r)#y ahora me imprime la nueva lista

#r.extend((11,12))#extend hace lo mismo que append, solo que me los muestras como valores indivuduales. Una tupla para que me tome los dos valores, y no mande error
#print(r)
#r.insert(len(r), 13)#aqui toma la longitud e inserto el valor al final
#print(r)
#r.clear#clear me limpia la lista, borra todos los elementos 

#r.sort(reverse=True)#lo que esto hace es ordenarlos alfabeticamente, pero a la inversa, osea comenzando por la z
#print(r.index(10))#me imprime el indice del valor dado (10) en este caso

"""Tuplas"""

#las tuplas son casi iguales a las listas, solo que las tuplas no se pueden cambiar

#x = (1,2,3)#esto es una tupla
#print(x)

#y = tuple((1,2,3,4,5,6))
#print(y)

"""Sets"""
#set es una coleccion desordenada, sin un indice
#colors = {"red" "green" "blue"}
# colors.add("violet")
#print(colors)

"""Diccionarios"""
# product = { #esto es un diccionario
#     "name": "book",
#     "cantidad":3,
#     "precio": 4.99
# }
# person = { #sirven para plasmar objetos de la vida real
#     "nombre":"ryan",
#     "apellido":"perez"
# }
# print(person.keys())#muestro solo  las llaves
# print(person.items())#aqui muestro todo

# productos = [
#     {"name": "libro", "precio": 5.00},
#     {"name": "pc", "precio": 150},

# ]
# print(productos)

"""Condicionales"""

#if 
# name = "john"
# apellido = "carter"

# if name =="john":
#     if apellido =="carter":
#         print("tu eres jon carter")
#     else:
#         print("tu no eres john carter")
# else:
#     print("tu no eres john")

#for

# foods = ["pan","manzana","queso","leche","banano"]

# for food in foods:
#     if foods == "queso":
#         print("compra queso")
#     print(foods)
    #break #para que el codigo pare
    #continue #para que el codigo continue 

#for letra in "hola":
#   print(letra)#me muestra uno a uno las letras

#while
# x = 4

# while x <= 10:
#     print(x)
#     count =+1

"""Funciones"""

# def hola(nombre = "humano"):
#     print("Hola" + nombre)

# hola("esteban")

#add = lambda n1, n2: n1 + n2#esto es una funcion lambda, la cual no tiene nombre y retorna los valores por default(determinado)
#print(add(5+5))

"""Modulos o Bibliotecas"""

""" modulo descargado (pypi modules)"""
#ir a la pagina y descargar el modulo que quiera
#pip nos sirve para descargar modulos de terceros
#pip install colorama #asi se instala un modulo de terceros



"""modulo de python, o buscar python modulos"""
#import datetime
#print(datetime.date.today())#muestra la fecha 


""" modulo creado por uno mismo"""
#import empezando #asi importo un modulo propio
