"""frase = 'python es un gran lenguaje'

# para saber cuantas veces aparece un caracter en nuestro string usamos la funcion count.

frase.count('e')

# si queremos reemplazar un caracter por otro usamos la funcion replace usando la logica: frase.replace('letra a cambiar', 'letra nueva').
frase.replace('p', 'q')

# para separar nuestra string en una lista con todos los string segun un patron como el espacio entre palabras hacemos 

frase.split(' ') 

print(frase)
print(frase.count('e'))
print(frase.replace('p', 'q'))
print(frase.split(' '))"""


# Reto:

nombre = input('¿Cual es tu nombre compadre? ')

saludo = f'Hola {nombre}, es un placer conocerte compadrito '

print(saludo + '¿Sabias que la longitud de este texto es de?: ', len(saludo))