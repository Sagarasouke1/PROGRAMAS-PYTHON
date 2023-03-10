# Strings

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_other_string + " " + my_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un String  \\ nescapado"
print(my_scape_string)

# Formateo

name, surname, age = "Emanuel", "Simon", 26

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))

# Inferencia de datos
print(f"Mi nombre es {name} {surname} y mi edad es {age}".format(name, surname, age))

# Desempaquetado de caracteres

palabra = "python" # Definicion de variable
a,b,c,d,e,f  = palabra # Definicion de variable con igualdad a otra variable

print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Division

palabra_slic = palabra[1:3]
print(palabra_slic)

palabra_slic = palabra[1:4]
print(palabra_slic)

palabra_slic = palabra[-2]
print(palabra_slic)
palabra_slic = palabra[0:6:2]
print(palabra_slic)

# Reversa

reversa_palabra = palabra[::-1]
print(reversa_palabra)

# Funciones

print(palabra.capitalize())
print(palabra.upper())
print(palabra.count("t"))
print(palabra.isnumeric())
print("1".isnumeric())
print(palabra.lower())
print(palabra.startswith("py"))



