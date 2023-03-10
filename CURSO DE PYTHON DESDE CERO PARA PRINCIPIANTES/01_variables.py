# Variables

my_string_variable = 'My String variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea. ¡Cuidado con abusar de esta sintaxis!
nombre , surname, alias, age = "Emanuel", "Simon", "Rana", 26
print(nombre, surname, age, "y mi alias es:", alias)

# Inputs
"""
nombre = input('¿Cual es tu nombre?: ')
age = input('¿Cuantos años tienes? ')
print(nombre)
print(age)
"""

# Cambiamos su tipo
nombre = 26
age = "Emanuel"
print(nombre)
print(age)

# ¿Forzamos el tipo de variable?
direccion: str = "Mi dirección"
direccion = True
direccion = 5
direccion = 1.2
print(type(direccion))

