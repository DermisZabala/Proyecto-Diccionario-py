import json

dato = json.load(open("diccionario.json"))


def significado(p):
    if p in dato:
        return dato[p]
    else:
        return "La palabra no existe. Porfavor compruebalo dos veces"

palabra = input("Ingrese una palabra: ").lower()

print(significado(palabra))