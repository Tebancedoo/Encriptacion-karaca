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
    sin_e = sin_a.replace("e", "1")
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