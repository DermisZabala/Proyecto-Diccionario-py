import json
from difflib import SequenceMatcher, get_close_matches
import os
import pywhatkit
dato = json.load(open("diccionario.json"))


def significado(p):
    if p in dato:
        return dato[p]
    elif len(get_close_matches(p, dato.keys())) > 0:
        opcion = get_close_matches(p, dato.keys())[0]
        i = input("Quisiste decir {}? Ingresa 'S' si es asi de lo contrario ingrese 'N': " .format(opcion))
        if i.lower() == "s":
            print(opcion+":")
            return dato[opcion]
        elif i.lower() == "n":
            return "Entonces introduce la palabra correcta"
        else:
            return "No entiendo lo que introduciste"
    else:
        return "La palabra no existe. Porfavor compruebalo dos veces"

mensajeWhatsapp=[]


palabra = input("Escriba HAMEL para limpiar la pantalla y salir\nIngrese una palabra: ").lower()

while True:
    if palabra.lower() == "hamel":
        os.system("cls")
        break
    else:
        salida = significado(palabra)

    if type(salida)==list:
        contador = 1
        for i in salida:
            mensajeWhatsapp.append("{}. {}".format(contador, i))
            contador+=1
        
        mensaje = "\n".join(mensajeWhatsapp)
        
        try:            
            print("Mensaje que se enviara\n" + mensaje)
            # enviando el mensaje inmediatamente
            pywhatkit.sendwhatmsg_instantly("+18297940243", mensaje, wait_time=4)  # espera 4 segundos para abrir el whatsapp
            print("Mensaje Enviado") 
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    else: 
        print(salida)

    palabra = input("\nEscriba HAMEL para limpiar la pantalla y salir\nIngrese una palabra: ").lower()