import string

def crear_diccionario_compacto():
    """Crea el mismo diccionario de forma más concisa."""
    mapeo = {}
    
    # '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    caracteres = string.digits + string.ascii_uppercase
    
    # Asigna el índice (0 a 35) como el valor
    for indice, caracter in enumerate(caracteres):
        mapeo[caracter] = indice
        
    return mapeo

# Ejemplo:
diccionario_compacto = crear_diccionario_compacto()
# print(diccionario_compacto)
from statistics import mean
def has_exoplanet(readings):
    values = []
    for id in readings:
        values.append(diccionario_compacto[id])
    averege = mean(values)
    reading_less = []
    for id in readings:
        id_value = diccionario_compacto[id]
        if id_value <= (averege*0.8):
            reading_less.append(id_value)
    letters = [k for k, v in diccionario_compacto.items() if v in reading_less]
    print(letters)
    if reading_less:
        return True
    else:
        return False
print(has_exoplanet("665544554"))
print(has_exoplanet("FREECODECAMP"))