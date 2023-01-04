"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

x = 1
while x <= 100:
        if  x  % 3 == 0 and x % 5 == 0:
         print("fizzbuzz")
         x +=1
        elif x  % 3 == 0:
            print("fizz")
            x +=1
        elif x % 5 == 0:
            print("buzz")
            x +=1
        else:
            print(x)
            x +=1
"""
#recuerda esteban si en algun momento tienes que hacer una doble validacion esa va al inicio, por que si no el programa no la 
#va a tomar, debido a que alguna de las codiciones de arriba se van a cumplir
#fin el ejercicio 0

""" * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 


palabra1 = input("Favor ingrese una palabra:")#primero hago que el usuario ingrese las dos palabras
palabra2 = input("Favor ingrese otra palabra:")

list1 = list(palabra1)#luego convierto las palabras ingresadas por el usuario en listas 
list2 = list(palabra2)


sorted_list1 = sorted(list1)#con sorted se me ordena la lista alfabeticamente, y aqui ordeno las listas palabras alfabeticemente
sorted_list2 = sorted(list2)

if  sorted_list1 == sorted_list2:#y por ultimo aqui ya simplemente comparo las dos listas de palabras ordenadas
    print(True)
else:
    print(False)

"""
 #fin del 1 ejercicio
"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 

fibonacci = [0,1]#defino una lista donde se alojaran los numeros fibonacci, con el 0 y el 1 para despues sumarlos

for n in range(0,50):#despues le digo al bucle que se ejecute 50 veces para los 50 primeros numeros de la serie  
    numero1 = (fibonacci[-1]) #aqui digo que la variable numero1 va a ser igual al ultimo numero de la serie
    numero2 = (fibonacci[-2]) #aqui digo que la variable numero2 va a ser igual al penultimo numero de la serie
    n = numero1 + numero2 #y aqui digo que n va a ser igual al ultimo numero de la seria mas el penultimo numero de la serie

    if n == numero1 + numero2: #aqui ya simplemente digo que si n el igual a la suma de numero1 y numero2, que ingrese n en la serie
        fibonacci.append(n)#si la condicion se cumple n se incrusta en la serie fibonacci
print(fibonacci)#imprimo toda la serie
"""
#fin del 2 ejercicio

"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.

num = int(input("Favor ingrese un numero")) #aqui reviso si el numero ingresado es primo o no, y con el int hago que el pase a ser numeros

if num%3 == 0:#si el modulo de la variable num es cero imprime el numero es primo
    print("El numero es primo")
else:
    print("El numero no es primo")#de lo contrario imprime el numero no es primo

for n in range(0,100):#aqui creo un for con rango de 0 a 100
    if n%3 == 0:#y ya por ultimo si el modulo de 3 de n es cero me imprime el numero, si no, no lo implrime
        print(n)
"""
#fin del 3 ejercicio

#crea una funcion y no se te olvide llamarla al final para que se ejecute

"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.



def poligono():

  x = int(input("Favor ingrese su poligono: 1(cuadrado), 2(triangulo) 3(rectangulo)"))#aqui pido al usuario que ingrese un numero 
  if x == 1:
    print("un lado elevado al cuadrado")#aqui digo si el numero es ingresado es igual a 1(cuadrado) digo como se calcula el area del cuadrado
  elif x == 2:
    print("base por altura dividido 2")#aqui digo si el numero es ingresado es igual a 2(triangulo) digo como se calcula el area del triangulo
  elif x == 3:
    print("base por altura")#aqui digo si el numero es ingresado es igual a 3(rectangulo) digo como se calcula el area del rectanduglo
  else:
    print("favor seleccione un poligono")# y si no pasa nada de lo anterior digo al usuario que ingrese un pligono

poligono()#y por ultimo aqui llamo a la funcion para que se ejecute

"""
#fin del 4 ejercicio

"""
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
 *   mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.

def aspectRatio():
    imagen = input("favor ingrese url de la imagen a calcular el aspect ratio")
    
 """
#con este no pude por el momento (ejercicio 5)

""" 
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

def invertir():
    cadena = list(input("favor ingrese una cadena de texto:"))#aqui le digo a python que el string ingresado lo tome como lista, esto para que si lo imprimo me lo tome letra por letra 
    print(cadena[-1])#aqui digo que me imprima el ultimo valor
    print(cadena[-2])#aqui digo que me imprima el penultimo valor y asi sucesivamente
    print(cadena[-3])
    print(cadena[-4])
    print(cadena[-5])
    print(cadena[-6])
    print(cadena[-7])
    print(cadena[-8])
    print(cadena[-9])
    print(cadena[-10])
invertir()#aqui llamo a la funcion invertir 
 """
#fin del 6 ejercicio

"""
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 

def contar():
    lista_palabras = []
    palabra_buscar = input("favor ingrese la palabra que quiere contar: ")
    lista_palabras = input("Favor ingrese palabras para contar cuantas veces se repiten: ")
    if palabra_buscar in lista_palabras:#el in sirve para saber si algo esta dentro de otra cosa(en este caso una palabra en un array)
        print("True")
        print("Su palabra se encuentra: ")
        print(lista_palabras.count(palabra_buscar))#aqui estoy contando las veces que se encuentra la palabra ingresada por el usuario(palabra_busca) en la lista(lista_palabras)
        print("veces")
    else:
        print("False")
contar()
"""
#fin del 7 ejercicio

"""
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"

    binario = "" # Aquí almacenamos el resultado
    while decimal > 0: # Mientras se pueda dividir se ejecuta el while
        residuo = int(decimal % 2) # Saber si es 1 o 0
        decimal = int(decimal / 2) # E ir dividiendo el decimal
        binario = str(residuo) + binario # Ir agregando el número (1 o 0) a la izquierda del resultado
    return binario # devuelve el binario

decimal = int(input("Ingresa un número decimal: "))
binario = decimal_a_binario(decimal)
print(f"El número {decimal} es {binario} en binario")
 """
 #fin del 8 ejercicio pero este lo saque de google 

"""
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.


def morse_o_natural():
    opocion_realizar = input("Favor escirba si quiere pasar de natural a morse escribiendo (morse) o vicesersa escribiendo (natural)")
    if opocion_realizar == "morse":
        morse()
    else:
        opocion_realizar == "natural"
        natural()

a = ".""-"
b = "-""."".""."
c = "-"".""-""."
d = "-"".""."
e = "."
f = "."".""-""."
g = "-""-""."
h = ".""."".""."
i = ".""."
j = ".""-""-""-"
k = "-"".""-"
l = ".""-"".""."
m = "-""-"
n = "-""."
o = "-""-""-"
p =".""-""-""."
q = "-""-"".""-"
r = ".""-""."
s = "."".""."
t = "-"
u = "."".""-"
v = ".""."".""-"
w = ".""-""-"
x = "-""."".""-"
y = "-"".""-""-"
z = "-""-"".""."
espacio = " "

def morse():
    frase =  str(input("Escriba frase para cambiar a morse:"))
    if frase == "perro":
        print("Su frase en morse es:" + p,e,r,r,o)
    
def natural():
    frase2 =  str(input("Escriba frase para cambiar a natural:"))
    if frase2 == ".--. . .-. .-. ---":
        print("(perro) es su frase natural ")
morse_o_natural()
    
 """
# fin del ejercicio 9 pero falta darle mas alcance (por el momento solo funciona con perro)

""" 
* Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }


def balanceada():
    expresion = str(input("Favor ingrese su expresion: "))#un input que le pide al usuario que ingrese la expresion
    # corchetes = "[" + " " +"]"#esto no lo utilice en el codigo
    # parentesis = "(" + " " + ")"#esto no lo utilice en el codigo
    # llaves = "{" + " " + "}"#esto no lo utilice en el codigo
    if "(" and ")" in expresion :#aqui digo si hay un ( y ) en la expresion que ingreso al usuario, pasa al siguiente if
        if "{" and "}" in expresion  :#aqui digo si hay un { y } en la expresion que ingreso al usuario, pasa al siguiente if
            if "[" and "]" in expresion :#aqui digo si hay un [ y ]  en la expresion que ingreso al usuario, pasa al siguiente if
                print("Su expresion esta balanceada ")
            else: 
                print("Su expresion no tiene [] ") #else de []
        else:
            print("Su expresion no tiene { } ") #else de {}
    else:
        print("Su expresion no tiene () ") #else de ()
balanceada()
"""
# fin del ejercicio 10

"""
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.

def cadenas():
    str1 = str(input("Favor ingrese caracteres: "))# pido caracteres al usuario
    str2 = str(input("Favor ingrese caracteres diferentes: "))# pido caracteres al usuario pero esta vez tienen que ser distintos
    print(sorted(str1))#los ordeno alfabeticamente (reordeno) e imprimo
    print(sorted(str2))#los ordeno alfabeticamente (reordeno) e imprimo
cadenas()
"""
#fin del ejercicio 11

"""
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
 * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.


def palindromo():
    palabra = input("Favor ingrese su palabra (4 letras como maximo): ")#el usuario ingresa la palabra
    palabra_minuscula = palabra.lower()#paso la palabra a minuscula
    if palabra_minuscula[0] == palabra_minuscula[-1]: #si la primera letra es igual a la ultima paso al siguiente if
        if palabra_minuscula[1] == palabra_minuscula[-2]: #si la segudan letra es igual a la penultima paso al siguiente if
            if palabra_minuscula[2] == palabra_minuscula[-3]: #si la tercera letra es igual a la antepenultima paso al siguiente if
                print(True)
    else:
        print(False)
palindromo()
"""
#fin del ejercicio 12, pero falta darle mas alcance, por el momento solo funciona con 4 letras

"""
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.

def factorial():
    facto = int(input("Favor ingrese el numero para dar su factorial: "))
    result = 1
    for i in range(1,facto+1):
        result = result *i
    print("el factorial es ", end="") 
    print(result)
factorial()
"""
#fin del ejercicio 13, pero el for lo saque de google

"""
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información 
 * al respecto.


def Armstrong():
    cifra = int(input("Favor ingrese el numero de cifras de su numero: "))
    num = input("Favor ingrese su numero `Armstrong`: ")
    numeros_sumar = []
    for numero in num:
        numero = numero ** cifra
        numeros_sumar.append(numero)
        numeros_sumados = sum(numeros_sumar)
        if numeros_sumados == num:
            print("Su numero es armstrong")
        else:
            print("Su numero NO es armstrong")

Armstrong()
"""

#ejercicio 14 no pude, me falta hacer que la variable del for la exponga (exponente) con cifra 

"""
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd MM yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.


def calcular_dias():
    fecha1 = input("Ingrese la fecha mas baja con el formato (dia Mes año) ")#El usuario ingresa la fecha 1
    fecha2 = input("Ingrese la fecha mas alta con el formato (dia Mes año) ")#El usuario ingresa la fecha 2
    fecha1_dividida = fecha1.split()#divido la fecha 1 por espacios
    fecha2_dividida = fecha2.split()#divido la fecha 2 por espacios
    #print(fecha1_dividida,fecha2_dividida)#solo imprimo las fechas para ver y ya 
    #int_list1 = [int(i) for i in fecha1_dividida]#convierto la lista1 dividida a int pero aun no funciona
    #int_list2 = list(map(int, fecha2_dividida))#convierto la lista2 dividida a int pero aun no funciona

    int_lista1 = int((fecha1_dividida[0]))#aqui paso el valor 0 de la fecha 1 dividida a una variable y la menciono como int
    int_lista1_0 = int((fecha1_dividida[1]))#aqui paso el valor 1 de la fecha 1 dividida a una variable y la menciono como int
    int_lista1_1 = int((fecha1_dividida[2]))#aqui paso el valor 2 de la fecha 1 dividida a una variable y la menciono como int
    #aqui las variables de la lista 2
    int_lista2 = int((fecha2_dividida[0]))#aqui paso el valor 0 de la fecha 1 dividida a una variable y la menciono como int
    int_lista2_0 = int((fecha2_dividida[1]))#aqui paso el valor 1 de la fecha 1 dividida a una variable y la menciono como int
    int_lista2_2 = int((fecha2_dividida[2]))#aqui paso el valor 2 de la fecha 1 dividida a una variable y la menciono como int
    #ahora resto las variables para que me de la fecha 
    resultado1 = int_lista1 - int_lista2
    resultado2 = int_lista1_0 - int_lista2_0
    resultado3 = int_lista1_1 - int_lista2_2
    #ahora voy a imprimirlos resultados
    print(f"Faltan {resultado1} dias")#concateno el resultado con palabras
    print(f"Faltan {resultado2} meses")#concateno el resultado con palabras
    print(f"Faltan {resultado3} años")#concateno el resultado con palabras
calcular_dias()
"""
#fin del ejercicio 15 y pude solo sjjsjsjsjsj 

"""
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.


def title_case(phrase: str):

    list_word = [word[0].upper() + word[1::].lower() for word in phrase.split(" ")]
    return " ".join(list_word)

print(title_case("hola mundo"))
print(title_case("mOuRedEV bY brais mOUre."))
print(title_case("no a la manzanilla..."))
  
"""
#fin del ejercicio 16 pero lo saque de google por que no se como poner la primra letra de la segunda palabra en mayuscula

"""
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.


def carrera():
    array = []
    palabra = input("Ingrese la palabra jump o run ")#el usuario ingresa jump o run
    palabra2 = input("Ingrese la palabra jump o run ")#el usuario ingresa jump o run
    if palabra == "jump" or "run":# si la palabra ingresada es jump o run se guardar en el array
        array.append(palabra)#guarda la palabra en el array
        if palabra2 == "jump" or "run":# si la palabra ingresada es jump o run se guardar en el array
            array.append(palabra2)#guarda la palabra en el array
        else:
            print("Vuelva a intentarlo")# de lo contrario manda un mensaje de aviso
    else:
        print("Vuelva a intentarlo")# de lo contrario manda un mensaje de aviso
    #print(array) # aqui era solo para ver los valores del array
    pista = input("Ingrese suelo o valla ")#el usuario ingresa suelo o vallar para hacer las comparaciones
    pista2 = input("Ingrese suelo o valla ")#el usuario ingresa suelo o vallar para hacer las comparaciones
    if array[0] == "jump" and pista == "valla":#hago las comparaciones si el 0 valor del array el jump y el valor de pista es valla me ejecuta el otro if
        if array[1] == "run" and pista2 == "suelo":#si el valor 1 del array es run y el de pista2 es suelo, imprimo el atleta paso
            print("El atleta paso")
    elif array[0] == "run" and pista == "valla":# de lo contrario si el 0 valor del array es run y el de pista es vallar manda x
        print("X")
    elif array[0] == "jump" and pista == "suelo":# y si la anterior no se cumple, entoces si el valor 1 del array es jump y el de pista el suelo manda /
        print("/")
carrera()
"""
#fin del ejercicio 17, de una forma no manda nada

"""
 * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
 * y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 *    O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta.
 * Se podría representar con un vacío "", por ejemplo.


# elem = 0
# for i in range(filas):
#     fila = []
#     for j in range(columnas): # Todo esto es un codigo interesenta que vi en google, lo que hace es poner los numeors del 0 al 8 en la matriz 3x3
#         fila.append(elem)
#         elem += 1
#     matriz.append(fila)

def analizar_matriz():
    matriz = [
              ["X","O","O"],
              ["O","X","X"],  #informacion sacada de: https://pythondiario.com/2019/01/matrices-en-python-y-numpy.html
              ["O","O","O"]
            ]
    #print(matriz[0][0])#me imprime el elemento en la fila cero en la columna cero osea la primera X
    if matriz == " ":
        print("Nulo")
    else:
        if matriz[0][0] == matriz[0][1] and matriz[0][2]: #me analiza si toda la fila 1 es igual si no pasa al siguiente
            print(matriz[0][0])
        elif matriz[1][0] == matriz[1][1] and matriz[1][2] :#me analiza si toda la fila 2 es igual si no pasa al siguiente
            print(matriz[1][0])
        elif matriz[2][0] == matriz[2][1] and matriz[2][2]:#me analiza si toda la fila 3 es igual si no pasa al siguiente
            print(matriz[2][0])
        elif matriz[0][0] == matriz[1][0] and matriz[2][0]:#me analiza si toda la columna 1 es igual si no pasa al siguiente
            print([0][0])
        elif matriz[0][1] == matriz[1][1] and matriz [2][1]:#me analiza si toda la columna 2 es igual si no pasa al siguiente
            print([0][1])
        elif matriz[0][2] == matriz[1][2] and matriz [2][2]:#me analiza si toda la columna 3 es igual si no pasa al siguiente
            print([0][2])
        else:
            print("Empate")#si nada de lo anterior se cumple manda empate
analizar_matriz()
"""
#fin del ejercicio 18 y lo hice solooo

"""
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.

def conversor():
    days = int(input("Ingrese dias "))
    hours = int(input("Ingrese horas "))
    minutes = int(input("Ingrese minutos "))
    seconds = int (input("Ingese segundos "))
    days_mls = 8.64e+7 * days
    hours_mls = 3.6e+6 * hours
    minutes_mls = 60000 * minutes
    seconds_mls = 1000 * seconds
    print(days_mls)
    print(hours_mls)
    print(minutes_mls)
    print(seconds_mls)
conversor()
"""
#fin del ejercicio 19 

""""
 * Crea una función que sume 2 números y retorne su resultado pasados
 * unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que
 *   debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
 *   asíncrona, es decir, sin detener la ejecución del programa principal.
 *   Se podría ejecutar varias veces al mismo tiempo.

import  threading #importo la libreria
import  time #importo la libreria
def parando_tiempo():#inicia la funicon parando tiempo
    valor1 = int(input("Ingrese primer valor "))#el usuario ingresa un valor
    valor2 = int(input("Ingese segundo valor "))#el usuario ingresa un valor
    valor3 = valor1 + valor2 #los valores se suman
    tiempo = int(input("Ingese tiempo que quiere que se demore la operación ")) #el usuario ingresa el tiempo
    time.sleep(tiempo)#el valor ingresado por el usuario se guarda en la variable y este el el parameto de la funcion time.sleep
    t = threading.Timer(tiempo, print(valor3))#no se que hace pero sirve 
    t.start()#inicia la funcion t 
parando_tiempo()#llamo la funcion parando tiempo
"""
#fin del ejercicio 20

"""
 * Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
 * resultado e imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un
 *   símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*"
 *   y división "/".
 * - El resultado se muestra al finalizar la lectura de la última
 *   línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han
 *   podido resolver las operaciones.

def calculadora():
    num1 = int(input("Favor ingrese un numero "))
    num2 = int(input("Favor ingrese otro numero "))
    operacion = str(input("Suma (+), Resta (-), Multiplicacion(*), Division(/) "))
    if operacion == "+" :
        suma = num1 + num2
        print(suma)
    elif operacion == "-":
        resta = num1 - num2
        print(resta)
    elif operacion == "*":
        multi = num1 * num2
        print(multi)
    elif operacion == "/":
        div = num1 / num2
        print(div)
    else:
        print("No se ha podido resolver la operacion")
calculadora()
"""
#fin del ejercicio 21

"""
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.


def buscar():
    array1 = list(input("Ingrese el array 1: "))
    array2 = list(input("Ingrese el array 2: "))
    boolean = bool(input("Ingrese el valor del booleano: "))
    if boolean == True:
        res = list(set(array1) & set(array2))#me busca y me guarda los valores comunes en los dos array
        print(res)
    elif boolean == False:
        no_esta = [i for i in array1 if i not in array2]# me busca y me guarda los valores no comunes en los dos array
        print(no_esta)
    else:
        print("Vuelva a intentarlo")
buscar()
"""
#fin del ejericico 22, peor el elif aun no funciona del todo

"""
 * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
 * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que 
 *   lo resuelvan directamente.

def mcd(num1: int, num2: int):

    Se realiza el cálculo del mcd se realiza mediante el algoritmo de Euclides.
    
    # Se debe determinar el número mayor para asignar a las variables a y b
    if num1 > num2:
        a = num1
        b = num2

    else:
        a = num2
        b = num1

    # Mientras b sea distinto de cero se realiza la operación
    while b:
        mcd = b
        b = a % b
        a = mcd

    # Imprime el valor del mcd
    print(f"El M.C.D de {num1} y {num2} es {mcd}")

    return mcd


def mcm(num1: int, num2: int):
    # Calcula el mcm a partir del mcd y lo imprime
    print(f"El M.C.M de {num1} y {num2} es {(num1*num2) // mcd(num1, num2)}")


# Tests
mcm(10, 5)
mcm(8, 7)
mcm(1, 2)
mcm(21, 17)
"""
#fin del ejercicio 23, pero lo saque de internet 

"""
 * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 * ¿De cuántas maneras eres capaz de hacerlo?
 * Crea el código para cada una de ellas.

#primera forma
for x in range(1,101):
    print(x)
#segunda forma
y = 0
while y <= 100:
    print(y)
    y +=1  
#tercer forma
lista_numeros = []
for num in range(1,101):
    lista_numeros.append(num)
    print(num)
"""
#fin del ejercicio 24

"""
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 *   o "S" (tijera).
 * - Ejemplo. Entrada: ["R","S"] ["S","R"] ["P","S"]. Resultado: "Player 1".

def ganador_partidas():
    resultados = list(input("Ingrese los resultados de la partida: "))
    if resultados[2] == resultados[6]:
        print("Tie")
    elif resultados[2] == "R" and resultados[6] == "S":#reviso posicion del array parte por parte
        print("Player 1")
    elif resultados[2] == "S" and resultados[6] == "R":
        print("Player 2")
    elif resultados[2] == "P" and resultados[6] == "R":#reviso posicion del array parte por parte
        print("Player 1")
    elif resultados[2] == "R" and resultados[6] == "P":
        print("Player 2")
    
    elif resultados[12] == resultados[16]:
        print("Tie")
    elif resultados[12] == "R" and resultados[16] == "S":
        print("Player 1")
    elif resultados[12] == "S" and resultados[16] == "R":#reviso posicion del array parte por parte
        print("Player 2")
    elif resultados[12] == "P" and resultados[16] == "R":
        print("Player 1")
    elif resultados[12] == "R" and resultados[16] == "P":#reviso posicion del array parte por parte
        print("Player 2")
    
    elif resultados[22] == resultados[26]:
        print("Tie")
    elif resultados[22] == "R" and resultados[26] == "S":#reviso posicion del array parte por parte
        print("Player 1")
    elif resultados[22] == "S" and resultados[26] == "R":
        print("Player 2")
    elif resultados[22] == "P" and resultados[26] == "R":#reviso posicion del array parte por parte
        print("Player 1")
    elif resultados[22] == "R" and resultados[26] == "P":
        print("Player 2")
ganador_partidas()
"""
#fin del ejercicio 25

"""
 * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?

import turtle
def dibujar_figuras():
    figura = int(input("1: Circulo 2: Triangulo 3:Rectangulo 4:Cuadrado "))#Creo las opciones

    if figura == 1:
        tamaño = int(input("Ingrese el tamaño del circulo: "))#hago los if o elif correspondientes
        print(turtle.circle(tamaño))

    elif figura == 2:
        simbolo = '*'
        tamaño = int(input("Ingrese el tamaño del triangulo: "))#hago los if o elif correspondientes
        for i in range(tamaño):
            print(simbolo * i)

    elif figura == 3:#hago los if o elif correspondientes
        for i in range(2):
            turtle.forward(20)
            turtle.right(90)
            turtle.forward(10)
    else:
        simbolo = '*'
        tamaño = int(input("Ingrese el tamaño del cuadrado: "))#hago los if o elif correspondientes
        for i in range(tamaño):
            print(simbolo * tamaño)
dibujar_figuras()
"""
#fin del ejercicio 26, pero unos los saque de internet

"""
 * Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]

def vector_ortogonal():
    vector1 = input("Ingrese su vector 1 (los dos vectores deben tener la misma longitud): ")
    vector2 = input("Ingrese su vector 2 (los dos vectores deben tener la misma longitud): ")
    print(vector1[0])
    resultado_vectores = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
    if resultado_vectores == 0:
        print("Los vectores si son ortogonales")
    else:
        print("Los vectores no son ortogonales")
vector_ortogonal()
"""
#fin del ejercicio 27, pero falta la operacion de la linea 778

"""
 * Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (array de monedas) y un número que indique la selección
 * del producto.
 * - El programa retornará el nombre del producto y un array con el dinero
 *   de vuelta (con el menor número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe,
 *   deberá indicarse con un mensaje y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas
 *   de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.


def maquina_expendedora():
    monedas = [] #array donde se guardara el salgo del comprador mas adelante
    mone = int(input("Ingrese su saldo para comprar el producto: "))#pido al usuario que ingrese su saldo
    if mone == 5 or 10 or 50 or 100 or 200:#el salgo solo puede ser los valores mencionados 5,10,50,100 o 200
        producto = int(input("ingrese el numero de su producto 1:papas, 2:Chocolatina, 3:Bebida, 4:Choclitos, 5:Mani: ")) #el usuario escoje el producto a comprar
        if producto == 1: #si  el producto es 1 hace lo siguiente
            if mone < 5:#si el saldo ingresado es menor a el valor del producto muestra le falta dinero
                print("Le falta dinero")
            else:
                print("Usted compro papas de pollo")#de lo contrario se hizo la compra y el dinero del usuario se le resta el precio del producto para despues ingresarlo al list e imprimirlo
                new = mone - 5
                monedas.append(new)
                print(monedas)
        elif producto == 2:#si  el producto es 2 hace lo siguiente
            if mone < 10:#si el saldo ingresado es menor a el valor del producto muestra le falta dinero
                print("Le falta dinero")
            else:
                print("Usted compro Chocolatina")#de lo contrario se hizo la compra y el dinero del usuario se le resta el precio del producto para despues ingresarlo al list e imprimirlo
                new = mone - 10
                monedas.append(new) 
                print(monedas)
        elif producto == 3:#si  el producto es 3 hace lo siguiente
            if mone < 50:#si el saldo ingresado es menor a el valor del producto muestra le falta dinero
                print("Le falta dinero")
            else:
                print("Usted compro una bebida")#de lo contrario se hizo la compra y el dinero del usuario se le resta el precio del producto para despues ingresarlo al list e imprimirlo
                new = mone - 50
                monedas.append(new) 
                print(monedas)
        elif producto == 4:#si  el producto es 4 hace lo siguiente
            if mone < 100:#si el saldo ingresado es menor a el valor del producto muestra le falta dinero
                print("Le falta dinero")
            else:
                print("Usted compro choclitos")#de lo contrario se hizo la compra y el dinero del usuario se le resta el precio del producto para despues ingresarlo al list e imprimirlo
                new = mone - 100
                monedas.append(new) 
                print(monedas)
        elif producto == 5:#si  el producto es 5 hace lo siguiente
            if mone < 200:#si el saldo ingresado es menor a el valor del producto muestra le falta dinero
                print("Le falta dinero")
            else:
                print("Mani")#de lo contrario se hizo la compra y el dinero del usuario se le resta el precio del producto para despues ingresarlo al list e imprimirlo
                new = mone - 200
                monedas.append(new) 
                print(monedas)
        else:
            print("Algo fallo")
            print(mone)
    else:
        print("Moneda invalida")
maquina_expendedora() 
"""
#fin del ejercicio 28

"""
 * Crea una función que ordene y retorne una matriz de números.
 * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
 *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 *   o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 *   automáticamente.

def ordenar_lista(lista,ordenar):#declaro los parametros
    if ordenar == "asc":#si ordenar es igual a asc "ascendente" los numeros se ordenan de forma ascendente
        lista.sort()#la lista se ordena de forma ascendente o creciente es lo mismo
        print(lista)#imprimo la lista
    elif ordenar == "desc":#si ordenar es igual a desc "descendiente" la lista de ordena de forma descendente
        lista.sort(reverse=True)#la lista se ordena de forma descendente
        print(lista)#imprimo la lista 
    else:
        print("Ha ocurrido un error")#por si lo anterior no sirve

#pruebas
ordenar_lista([2, 4, 6, 8, 9],"desc")#parametros
ordenar_lista([2, 1, 6, 5, 3],"asc")#parametros
"""
#fin del ejercicio 29 

"""
 * Crea una función que reciba un texto y muestre cada palabra en una línea,
 * formando un marco rectangular de asteriscos.
 * - ¿Qué te parece el reto? Se vería así:
 *   **********
 *   * ¿Qué   *
 *   * te     *
 *   * parece *
 *   * el     *
 *   * reto?  *
 *   **********

def marco_palabras(texto):
    lista_de_palabras = texto.split()
    for palabra in lista_de_palabras:
        print("* " + palabra + " *")

marco_palabras("esto es una prueba")
"""
#fin del ejercicio 30, me falto una parte de los *** y tengo que usar mas el for

"""
 * Crea una función que imprima los 30 próximos años bisiestos
 * siguientes a uno dado.
 * - Utiliza el menor número de líneas para resolver el ejercicio.

def bisiesto(año):#inicio de la funcion
    if año % 4 == 0:#si el año ingresado al dividirlo por 4 da cero imprime el año ingresado es bisiesto
        print(f"El año: {año} es bisiesto")#imprime el mensaje
        for año in range(año,año+120):#multiplique 4 por 30 (porque tengo que imprimir los años bisiestos, multiplos de 4 y los proximos 30 años bisiestos)
            if año % 4 == 0:#me calcula cada numero de la vuelta del for y si es divisible por 4 y su resto da cero me imprime ese numero
                print(año, end=" ")#imprime el año y cuando llega a " " se acaba todo
    else:
        print("El año no es bisiesto")#lo imprime si el año no es bisiesto
bisiesto(2012)#llamado de la funcion
"""
#fin del ejercicio 31

"""
 * Dado un listado de números, encuentra el SEGUNDO más grande.

def segundo_grande(num):#inica la funcion con el parametro
    second_number = sorted(num)#ordeno los numeros de menor a mayor
    print(second_number[-2])#imprimo el penultimo numero, el cual es el segundo mas grande
segundo_grande([28,22,24,11,14,6])#llamo la funcion con el parametro
"""
#fin del ejercicio 32

"""
 * Enunciado: Crea un función, que dado un año, indique el elemento 
 * y animal correspondiente en el ciclo sexagenario del zodíaco chino.
 * - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
 * - El ciclo sexagenario se corresponde con la combinación de los elementos
 *   madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
 *   conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
 *   (en este orden).
 * - Cada elemento se repite dos años seguidos.
 * - El último ciclo sexagenario comenzó en 1984 (Madera Rata).

def zodiaco_chino(año):
    elementos = ["madera", "fuego", "tierra", "metal", "agua", ]#lista elementos
    animales = ["rata", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo", "oveja", "mono", "gallo", "perro", "cerdo"]#lista animales
    
    offset = año - 1984 % 60

    elemento = elementos[offset % (len(elementos) * 2) // 2]
    animal = animales[offset % len(animales)]

    return elemento, animal

if __name__ == '__main__':
    for año in range(1924, 1984):
        print(año, zodiaco_chino(año))

zodiaco_chino(año)
"""
#fin del ejercicio 33, pero lo saque de github

"""
 * Enunciado: Dado un array de enteros ordenado y sin repetidos, 
 * crea una función que calcule y retorne todos los que faltan entre
 * el mayor y el menor.
 * - Lanza un error si el array de entrada no es correcto.


def numero_entre(lista):
    lista2 = []#creo la lista2
    for x in range(lista[0], lista[-1] + 1):#hago un for con el rango del primer digito de la lista y el ultimo + 1
        lista2.append(x)# x ingresa a la lista 2
        if lista != lista2:# si la lista es diferente a la lista2, imprime la lista 1 y la lista 2
            print(lista,lista2)#imprime las dos listas
        else:
            print("a la lista no le faltan numeros")
            
numero_entre([1,3,5,6,8])#llamo a la funcion con el parametro
"""
#fin del ejercicio 34, pero lo que hace es imprimir la lista ingresada y la lista completa, para que el usuario mire que numeros faltan

"""
 * Enunciado: Crea un programa que calcule el daño de un ataque durante
 * una batalla Pokémon.
 * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
 *   (buscar su efectividad)
 * - El programa recibe los siguientes parámetros:
 *  - Tipo del Pokémon atacante.
 *  - Tipo del Pokémon defensor.
 *  - Ataque: Entre 1 y 100.
 *  - Defensa: Entre 1 y 100.

def daño_pokemon(atacante,defensor,ataque,defensa):#defino la funcion con sus parametros

    if atacante == defensor:#si el atacante es igual al defensor la efectividad es de 0.5
        efectividad = 0.5

    elif atacante  == "fuego" or "electrico" and  defensor == "agua" or "planta":#si el atacante es fuego o electrico y la defensa de agua o planta la efectividad es de 2
        efectividad = 2

    else:#en cualquier otro caso la efectividad es de 1
        efectividad = 1
    daño = 50 * (ataque / defensa) * efectividad#el daño es igual a la formula presentada

    print(f"El daño de ataque fue de: {daño} ")#concatene un string con el daño el cual es float

daño_pokemon("fuego","agua",50,50)#un pokemon mas debil que otro no puede tener la misma defensa que el ataque del que es mas fuerte
"""
#fin del ejercicio 35

"""
 * Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales
 * a Sauron contra otras bondadosas que no quieren que el mal reine
 * sobre sus tierras.
 * Cada raza tiene asociado un "valor" entre 1 y 5:
 * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
 *   Númenóreanos (4), Elfos (5)
 * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
 *   Huargos (3), Trolls (5)
 * Crea un programa que calcule el resultado de la batalla entre
 * los 2 tipos de ejércitos:
 * - El resultado puede ser que gane el bien, el mal, o exista un empate.
 *   Dependiendo de la suma del valor del ejército y el número de integrantes.
 * - Cada ejército puede estar compuesto por un número de integrantes variable
 *   de cada raza.
 * - Tienes total libertad para modelar los datos del ejercicio.
 * Ej: 1 Peloso pierde contra 1 Orco
 *     2 Pelosos empatan contra 1 Orco
 *     3 Pelosos ganan a 1 Orco

def anillos_poder(num_pelosos,num_sureños_b,num_enanos,num_numenoreanos,num_elfos,num_sureños_m,num_orcos,num_goblins,num_huargos,num_trolls):
#defino la funcion con los 10 parametros, los cuales son el numero de integrantes de cada especie

#defino el valor de los integrantes buenos 
    valor_pelosos = 1
    valor_sureños_b = 2
    valor_enanos = 3
    valor_numenoreanos = 4 
    valor_elfos = 5 

#defino el valor de los integrantes malos 
    valor_sureños_m = 2
    valor_orcos = 2 
    valor_goblins = 2 
    valor_huargos = 3 
    valor_trolls = 5

#multiplico el valor de cada especie con el numero de cada especie 
    pelosos = valor_pelosos * num_pelosos
    sureños_b = valor_sureños_b * num_sureños_b
    enanos = valor_enanos * num_enanos
    numenoreanos = valor_numenoreanos * num_numenoreanos
    elfos = valor_elfos * num_elfos

#multiplico el valor de cada especie con el numero de cada especie 

    sureños_m = valor_sureños_m * num_sureños_m
    orcos = valor_orcos * num_orcos
    goblins = valor_goblins * num_goblins
    huargos = valor_huargos * num_huargos
    trolls = valor_trolls * num_trolls

    buenos = pelosos + sureños_b + enanos + numenoreanos + elfos #sumo todo
    malos = sureños_m + orcos + goblins + huargos + trolls #sumo todo

    if buenos > malos:# si hay mas buenos que malos gana el bien, de lo contrario gana el mal
        print("Gana el bien")
    else:
        print("Gana el mal")
anillos_poder(5,8,9,4,5,6,2,1,3,4)
"""
#fin del ejercicio 36

"""
 * Enunciado: ¡Han anunciado un nuevo "The Legend of Zelda"! 
 * Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
 * Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos
 * "The Legend of Zelda" de la historia?
 * Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda
 * que tú selecciones.
 * - Debes buscar cada uno de los títulos y su día de lanzamiento 
 *   (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)

def zelda(zelda1, zelda2):
    #las fechas

    fecha1 = 16
    fecha2 = 7
    fecha3 = 2021
    fecha4 = 22
    fecha5 = 10 
    fecha6 = 2015

    #imprimo la fecha - otra fecha

    print("Han trasncurrido: ")
    print(f"{fecha4 - fecha1} Dias ")
    print(f"{fecha5 - fecha2} Meses ")
    print(f"{fecha3 - fecha6} años ")

zelda("The Legend of Zelda: Skyward Sword","The Legend of Zelda: Tri Force Heroes")
"""
#fin del ejercicio 37

"""
 * Enunciado: Crea un programa se encargue de transformar un número binario
 * a decimal sin utilizar funciones propias del lenguaje que 
 * lo hagan directamente.

def binario_decimal(numero_binario):
	numero_decimal = 0 

	for posicion, digito_string in enumerate(numero_binario[::-1]):#no entiendo el codigo del todo
		numero_decimal = int(digito_string) * 2 ** posicion

	print(f" El numero en decimal es : {numero_decimal}") 

binario_decimal("101")
"""
#fin del ejercicio 38, pero encerio necesito repasar mas el for

"""
 * Enunciado: Implementa uno de los algoritmos de ordenación más famosos:
 * el "Quick Sort", creado por C.A.R. Hoare.
 * - Entender el funcionamiento de los algoritmos más utilizados de la historia
 *   Nos ayuda a mejorar nuestro conocimiento sobre ingeniería de software.
 *   Dedícale tiempo a entenderlo, no únicamente a copiar su implementación.
 * - Esta es una nueva serie de retos llamada "TOP ALGORITMOS",
 *   donde trabajaremos y entenderemos los más famosos de la historia.

def QuickSort(arr):

    elements = len(arr)
    
    #Base case
    if elements < 2:
        return arr
    
    current_position = 0 #Position of the partitioning element

    for i in range(1, elements): #Partitioning loop
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp #Brings pivot to it's appropriate position
    
    left = QuickSort(arr[0:current_position]) #Sorts the elements to the left of pivot
    right = QuickSort(arr[current_position+1:elements]) #sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right #Merging everything together
    
    return arr

array_to_be_sorted = [4,2,7,3,1,6]
print("Original Array: ",array_to_be_sorted)
print("Sorted Array: ",QuickSort(array_to_be_sorted))

#https://www.genbeta.com/desarrollo/implementando-el-algoritmo-quicksort
"""
#fin del ejercicio 39, pero me falta repasar un poquito mas este y lo saque de internet

"""
 * Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal"
 * indicándole únicamente el tamaño del lado.
 *
 * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
 *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif

from math import factorial

def combinacion(n, r):
    return factorial(n)//(factorial(r)*factorial(n-r))

num = int(input("Introduce un número: "))

for n in range(num):
    row = []    
    for r in range(n+1):
        row.append(combinacion(n, r))
    print(' '*(num-n) + " ".join(str(e) for e in row))
"""
#fin del ejercicio 40, pero no pude tengo que mejorar haciendo bucles for

"""
 * Enunciado: Crea una función que calcule el valor del parámetro perdido
 * correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
 *   el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará
 *   la cadena de texto "Invalid values".

def ley_ohm(V,R):
    if V == " " or R == "":
        print("Invalid values")
    else:  
        corriente = V / R
        print(round(corriente,2))
ley_ohm(55,1)
"""
#fin del ejercicio 41 

"""
 * Enunciado: Crea una función que transforme grados Celsius en Fahrenheit
 * y viceversa.
 *
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°" 
 *   y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
 * - ¿Quieres emplear lo aprendido en este reto?
 *   Revisa el reto mensual y crea una App: 
 *   https://retosdeprogramacion.com/mensuales2022


def conversor_temperatura(grados,unidad):
    if unidad == "°C" :
        celsius = (grados * 9/5) + 32
        print(f"Los grado celsius son: {round(celsius,3)}°")

    elif unidad == "°F":
        fahrenheit = (grados - 32) * 5/9
        print(f"Los grados fahrenheit son: {round(fahrenheit,3)}°")
    else:
        print("Valores invalidos")

conversor_temperatura(1,"°F")    
"""
#fin del ejercicio 42

"""
 * Enunciado: Este es un reto especial por Halloween.
 * Deberemos crear un programa al que le indiquemos si queremos realizar "Truco
 * o Trato" y un listado (array) de personas con las siguientes propiedades:
 * - Nombre de la niña o niño
 * - Edad
 * - Altura en centímetros
 *
 * Si las personas han pedido truco, el programa retornará sustos (aleatorios)
 * siguiendo estos criterios:
 * - Un susto por cada 2 letras del nombre por persona
 * - Dos sustos por cada edad que sea un número par
 * - Tres sustos por cada 100 cm de altura entre todas las personas
 * - Sustos: 🎃 👻 💀 🕷 🕸 🦇
 *
 * Si las personas han pedido trato, el programa retornará dulces (aleatorios)
 * siguiendo estos criterios:
 * - Un dulce por cada letra de nombre
 * - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
 * - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
 * - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩


def truco_traco(palabra,nombres,edades,alturas):
    if palabra == "truco":#si la palabra es truco

        #empieza nombres

        letras_nombres1 = len(nombres[0])#guarda cuantas letras tiene el primer nombre ingresado
        letras_nombres2 = len(nombres[1])#guarda cuantas letras tiene el segundo nombre ingresado
        letras_nombres = round(letras_nombres1 + letras_nombres2 / 2)#sumo las 2 variables anteriores y las divido en 2 y las redondeo
        for i in range(0,letras_nombres - 3 ):#hago un for y le resto 3 para que me imprima los sustos que son
            print("👻")#imprimo el susto las veces que diga el for 

        #empieza edades

        contador_pares,  = 0, 
        # iterating each number in list
        for num in edades:
        # checking condition
            if num % 2 == 0:
                contador_pares += 1 #hago un contador para saber cuantos numeros pares hay e imprimo esos sustos 
                for i in range(0,contador_pares):
                    print ("💀 🕷")
                

        #empieza alturas

        suma = sum(alturas)#sumo las alturas
        suma_alturas = round(suma / 100) #esas alturas las redondeo y divido en 100
        suma_alturas = suma_alturas * 2#las multipico por 2
        for i in range(0,suma_alturas):#y hago un for con el valor final la suma de las alturas 
            print("🕸 🦇")#imprimo los sustos

    elif palabra == "trato":

        #empieza letras
        letras_nombres1 = len(nombres[0])#guarda cuantas letras tiene el primer nombre ingresado
        letras_nombres2 = len(nombres[1])#guarda cuantas letras tiene el segundo nombre ingresado
        letras_nombres = round(letras_nombres1 + letras_nombres2 )#sumo las 2 variables anteriores y las divido en 2 y las redondeo
        for i in range(0,letras_nombres):#hago un for y le resto 3 para que me imprima los dulces que son
            print("🍡")#imprimo los dulces las veces que diga el for 

        # empieza edades
        suma_edades = sum(edades)# suma las edades
        if suma_edades >= 20:#como el maximo de personas que yo puse fueron 2 no se puede imprimir mas de 6 dulces
            for i in range (1,7):#hago el for que imprime 6 dulces por las 2 personas
                print("🍫")

        #empieza alturas

        suma = sum(alturas)#sumo las alturas
        suma_alturas = round(suma / 50)#redondeo las alturas y las divido por 50
        for i in range(0,suma_alturas):#el for imprime 2 dulces cada 50 cm de altura entre los dos
            print("🧁 🍩")#imprimo los dulces
        
truco_traco("trato",["juan","pedro"],[10,18],[130,175])    
"""
#fin del ejercicio 43, pero solo funciona bien con 2 personas, ese fue el limite que le puse

"""
 * Enunciado: Crea una función que retorne el número total de bumeranes de 
 * un array de números enteros e imprima cada uno de ellos.
 * - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números
 *   seguidos, en el que el primero y el último son iguales, y el segundo
 *   es diferente. Por ejemplo [2, 1, 2].
 * - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2] 
 *   y [4, 2, 4]).

def bumeranes(lista):
    total_numeros_lista = len(lista)#miro cuantos valores tiene lista y lo guardo en una variable
    for x in range(0,total_numeros_lista):#hago un for desde cero hasta el valor maximo dela lista 
        if lista[x] == lista[-x] and lista[x] != lista[x + 1]:#si el primer valor es igual al ultimo y el primer valor es diferente al segundo imprima buemeran
            print("Bumeran")#imprime 1 bumeran por cada bumeran que haya
    print(lista)
bumeranes([1,2,1,4,5,4])
"""
#fin del ejercicio 44, pero tiene una limitacion, los bumeranes tiene que ser con numeros distintos

"""
 * Enunciado: Dado un array de números enteros positivos, donde cada uno
 * representa unidades de bloques apilados, debemos calcular cuantas unidades
 * de agua quedarán atrapadas entre ellos.
 *
 * - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
 *
 *         ⏹
 *         ⏹
 *   ⏹💧💧⏹
 *   ⏹💧⏹⏹💧⏹
 *   ⏹💧⏹⏹💧⏹
 *   ⏹💧⏹⏹⏹⏹
 *
 *   Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades
 *   de agua. Suponemos que existe un suelo impermeable en la parte inferior
 *   que retiene el agua.


def unidades_de_agua(lista):
    altura = 0
    cantidad_agua = 0

    while True:

        espacio_libre = 0
        bloque_izquierda = -1
        bloque_derecha = -1

        for j in range(len(lista)):
            if lista[j] > altura:
                if bloque_izquierda == -1:
                    bloque_izquierda = j

                bloque_derecha = j
                espacio_libre += 1

        if (bloque_izquierda != 1) and (espacio_libre != (bloque_derecha - bloque_izquierda + 1)):
            cantidad_agua += (bloque_derecha - bloque_izquierda + 1) - espacio_libre
        else:
            break

        altura += 1

    return (cantidad_agua)


if __name__ == "__main__":
    lista = [4, 0, 3]
    print(f"Hay {unidades_de_agua(lista)} unidades de agua")

    lista = [4, 0, 3, 6, 1, 3]
    print(f"Hay {unidades_de_agua(lista)} unidades de agua")

    lista = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print(f"Hay {unidades_de_agua(lista)} unidades de agua")
"""
#fin del ejercicio 45, pero lo saque de github, no se me ocurrio nada en 3 dias

"""
 * Enunciado: Calcula dónde estará un robot (sus coordenadas finales) que se
 * encuentra en una cuadrícula representada por los ejes "x" e "y".
 * - El robot comienza en la coordenada (0, 0).
 * - Para idicarle que se mueva, le enviamos un array formado por enteros 
 *   (positivos o negativos) que indican la secuencia de pasos a dar.
 * - Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos, se detiene,
 *   luego 5, se detiene, y finalmente 2. 
 *   El resultado en este caso sería (x: -5, y: 12)
 * - Si el número de pasos es negativo, se desplazaría en sentido contrario al
 *   que está mirando.
 * - Los primeros pasos los hace en el eje "y". Interpretamos que está mirando
 *   hacia la parte positiva del eje "y".
 * - El robot tiene un fallo en su programación: cada vez que finaliza una
 *   secuencia de pasos gira 90 grados en el sentido contrario a las agujas
 *   del reloj.

def robot(lista):
    if len(lista) == 3:      #cuando el robot gira 90 grados siempre va a mirar al contrario por eso ultiplico el numero por -1, para que me de el mismo numero pero con signo opuesto
        ejey = lista[0]
        ejex = lista[1] * -1
        valory = lista[2] * -1
        Ejey = lista[0] + valory
        print(f"X: {ejex} Y: {Ejey}")
    else:
        print("Longitud de cordenadas no soportadas")
robot([10, -10, 2])
"""
#fin del ejercicio 46, pero solo soporto que se ingresen 3 numeros de cordenadas, tengo que agrandar el rango 

"""
 * Enunciado: Crea un función que reciba un texto y retorne la vocal que
 * más veces se repita.
 * - Ten cuidado con algunos casos especiales.
 * - Si no hay vocales podrá devolver vacío. 

def vocal_comun(texto):
    vocal_a = texto.count("a")
    vocal_e = texto.count("e")
    vocal_i = texto.count("i")
    vocal_o = texto.count("o")
    vocal_u = texto.count("u")

    print(f"En el texto hay {vocal_a} a ")
    print(f"En el texto hay {vocal_e} e ")
    print(f"En el texto hay {vocal_i} i ")
    print(f"En el texto hay {vocal_o} o ")
    print(f"En el texto hay {vocal_u} u ")

vocal_comun("oso coso")
"""
#fin del ejercicio 47,  tengo que tomar cursos de python, hay varias ocasiones donde se que es lo que tengo que hacer, pero no se como 

"""
 * ¿Conoces el calendario de adviento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software,
 * ciencia y tecnología desde el 1 de diciembre.
 *
 * Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne
 * lo siguiente:
 * - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo
 *   de ese día (a tu elección) y cuánto queda para que finalice el sorteo de ese día.
 * - Si la fecha es anterior: Cuánto queda para que comience el calendario.
 * - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.
 *
 * Notas:
 * - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00
 *   y finaliza a las 23:59:59.
 * - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos
 *   y segundos.
 * - 🎁 Cada persona que aporte su solución entrará en un nuevo sorteo
 *   del calendario de aDEViento hasta el día de su corrección
 *   (sorteo exclusivo para quien entregue su solución).


def adviento(fecha):
    if fecha < 1122022:
        print("Tienes que esperar hasta el 05/12/2022")
    else:
        if fecha > 24122022:
            print(round((fecha - 24122022) / 1000000))
        else:
            if fecha >= 1122022 and fecha <= 24122022:
                dict_fechas = {
                    1122022: "Has ganado un Pc Gamer",
                    2122022: "Has ganado un libro",
                    3122022: "Has ganado un mouse",
                    4122022: "has ganado un teclado",
                    5122022: "Has ganado una camisa",
                    6122022: "has ganado un control de PS1",
                    7122022: "Has ganado una consola de videojuegos",
                    8122022: "Has ganado unos stikers",
                    9122022: "Has ganado un par de tennis",
                    10122022: "Has ganado un par de almohadas",
                    11122022: "Has ganado un posillo personalizado",
                    12122022: "Has ganado un muñeco",
                    13122022: "Has ganado un collar",
                    14122022: "Has ganado un pantalon",
                    15122022: "Has ganado un videojuego",
                    16122022: "Has ganado un curso",
                    17122022: "Has ganado un pack de libros",
                    18122022: "Has ganado una licencias de Popsy",
                    19122022: "Has ganado un libro de inteligencia matematica",
                    20122022: "Has ganado un curso de Flutter",
                    21122022: "Has ganado el libro que puede salir mal",
                    22122022: "Has ganado 15 dolares para un dominio",
                    23122022: "Has ganado el libro codigo sostenible",
                    24122022: "Has ganado el libro codigo limpio",
                }
            print(dict_fechas[fecha])
adviento(5122022)
adviento(412022)
adviento(30122022)
"""
#fin del ejercicio 48, pero para avanzar me salte como 3 requerimientos de las instrucciones

"""
 * Enunciado: Crea una función que sea capaz de detectar y retornar todos los
 * handles de un texto usando solamente Expresiones Regulares.
 * Debes crear una expresión regular para cada caso:
 * - Handle usuario: Los que comienzan por "@"
 * - Handle hashtag: Los que comienzan por "#"
 * - Handle web: Los que comienzan por "www.", "http://", "https://" 
 *   y finalizan con un dominio (.com, .es...)


def handles(texto):
    handle_usuario = texto.count("@")
    handle_hastag = texto.count("#")
    handle_web = texto.count("www")
    handle_web2 = texto.count("http://")
    handle_web3 = texto.count("https://")
    handle_web4 = texto.count(".com")
    handle_web5 = texto.count(".es")
    print(f"handle usuario: {handle_usuario}, handle hastag: {handle_hastag}, handle web (www): {handle_web}, handle web(https://): {handle_web2} ")
    print(f"handle web (https://): {handle_web3}, handle web (.com): {handle_web4} y handle web (.es): {handle_web5}")
handles("dracoperez@, https://casas.com, www.http://comida.es, #programando,")
"""
#fin del ejercicio 49, pero me faltaron muchos handles

"""
 * Enunciado: Crea una función que sea capaz de encriptar y desencriptar texto
 * utilizando el algoritmo de encriptación de Karaca 
 * (debes buscar información sobre él).
"""
#defino la funcion
def karaca(texto, valor):

    #valor es la palabra encriptar o desencriptar

  if valor == "encriptar":

    #paso el texto a minusculas

    texto_minuscula = texto.lower()

    #reemplazo las vocales por numeros

    #0 = a
    #1 = e
    #2 = i
    #3 = o
    #4 = u
    sin_a = texto_minuscula.replace("a", "0")
    sin_e = sin_a.replace("e", "1")#replace es para reemplazar un valor por otro
    sin_i = sin_e.replace("i", "2")
    sin_o = sin_i.replace("o", "3")
    sin_u = sin_o.replace("u", "4")
    texto_encriptado = sin_u

    print(f"el texto encriptado es: {texto_encriptado}")
    #hago lo mismo para desencriptar

  elif valor == "desencriptar":

    texto_minuscula = texto.lower()
    con_a = texto_minuscula.replace("0","a")
    con_e = con_a.replace("1","e")
    con_i = con_e.replace("2","i")
    con_o = con_i.replace("3","o")
    con_u = con_o.replace("4","u")
    texto_desencriptado = con_u
    print(f"el texto desencriptado es: {texto_desencriptado}")

karaca("dr0c3","desencriptar")


""" PASOS
1. Pensar en que quiero o tengo que hacer
2. Plasmar la idea que tenga
3. Buscar en google si es necesario
4. Solucionar los errores
5. Terminar
"""
