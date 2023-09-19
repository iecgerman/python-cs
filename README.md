# python-cs
Curso de Introducción al Pensamiento Computacional con Python


# Cadenas y entradas 7/31
https://platzi.com/clases/1764-python-cs/25232-cadenas-y-entradas/

>>> my_str = 'Platzi'
>>> len(my_str)
6
>>> my_str[0]
'P'
>>> my_str[1]
'l'
>>> my_str[2]
'a'
>>> my_str[2:]
'atzi'
>>> my_str[:3]
'Pla'
>>> my_str[:-2]
'Plat'
>>> my_str[::2]
'Paz'
>>> 'To amo a ' + my_str
'To amo a Platzi'
>>> 
>>> 
>>> f'Yo amo a {my_str}'
'Yo amo a Platzi'
>>> f'Yo amo a {my_str},  '*100
'Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  Yo amo a Platzi,  '
>>> nombre = input('Cual es tu nombre: ')
Cual es tu nombre: Germán
>>> nombre
'Germán'
>>> print(nombre)
Germán
>>> print('Tu nombre es', nombre)
Tu nombre es Germán
>>> print(f'Tu nombre es {nombre}')
Tu nombre es Germán
>>> numero = input('escribe un numero: ')
escribe un numero: 45
>>> numero
'45'
>>> print(type(numero))
<class 'str'>
>>> numero = int(input('Escribe un número: '))
Escribe un número: 35
>>> print(type(numero))
<class 'int'>
>>> 
