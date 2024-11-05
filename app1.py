import json
from difflib import SequenceMatcher, get_close_matches

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

palabra = input("Ingrese una palabra: ").lower()

#print(SequenceMatcher(None, "hola", "hola").ratio())

#print(get_close_matches("rainn", ["help", "pyramid", "rain"]))

salida = significado(palabra)

if type(salida)==list:
    for i in salida:
        print(i)
else:
    print(salida)