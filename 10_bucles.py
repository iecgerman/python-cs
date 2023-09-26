"""
Los bucles, en diversos lenguajes de programación pueden ser definidos o indefinidos. Los bucles definidos preestablecen las condiciones de la iteración por adelantado. Por su parte, los bucles indefinidos establecen la condición en la que una iteración terminará. En este último tipo de bucles existe el riesgo de que el bucle se vuelva infinito (cuando la condición de suspensión nunca se cumple).

Los bucles definidos se implementan en Python a través del keyword for. Por su parte, los bucles indefinidos se implementan con el keyword while."""

frutas = ['manzana', 'pera', 'mango']

for fruta in frutas:
    print(fruta)

"""german@iecgerman:~/python-cs$ python3 10_bucles.py 
manzana
pera
mango"""

"""
Iterables

En Python, un iterable es un objeto que se puede utilizar en un bucle definido. Si un objeto es iterable significa que se puede pasar como argumento a la función iter. El iterable que se pasa como parámetro a la función iter
regresa un iterator."""

iter('cadena') # cadena
iter(['a', 'b', 'c']) # lista
iter(('a', 'b', 'c')) # tupla
iter({'a', 'b', 'c'}) # conjunto
iter({'a': 1, 'b': 2, 'c': 3}) # diccionario

frutas = ['manzana', 'pera', 'mango']
iterador = iter(frutas)
next(iterador)
manzana
next(iterador)
pera
next(iterador)
mango


""""
Bucles for con diccionarios

Para iterar a lo largo de un diccionario tenemos varias opciones:

    Ejecutar el bucle for directamente en el diccionario, lo cual nos permite
    iterar a lo largo de las llaves del diccionario.
    Ejecutar el bucle for en la llamada keys del diccionario, lo cual nos permite
    iterar a lo largo de las llaves del diccionario.
    Ejecutar el bucle for en la llamada values del diccionario, lo cual nos
    permite iterar a lo largo de los valores del diccionario.
    Ejecutar el bucle for en la llamada items del diccionario, lo cual nos
    permite iterar en una tupla de las llaves y los valores del diccionario.
"""

estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

for pais in estudiantes:
    ...

for pais in estudiantes.keys():
    ...

for numero_de_estudiantes in estudiantes.values():
    ...

for pais, numero_de_estudiantes in estudiantes.items():
    ...