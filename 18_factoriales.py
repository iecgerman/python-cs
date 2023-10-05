"""
esconocía totalmente que Python tuviera un límite de recursividad. Para conocerlo hay que importar la librería sys:

>>> import sys
>>> print(sys.getrecursionlimit())
1000

Para modificar ese límite

sys.setrecursionlimit(n) # n es el nuevo límite a establecer

"""

def factorial(n):

    # Siempre escribir nuestro docstring:

    """
    Calcual el factorial de n.

    n int > 0

    returns n!
    """
    print(n)
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

n = int(input('Escribe un entero: '))

print(factorial(n))

"""
Les comparto algo interesante que encontre en un libro.
Las funciones con llamadas recursivas utilizan memoria extra en las llamadas; existe un límite en las llamadas; existe un límite en las llamadas, que depende de la memoria de la computadora. En caso de superar este límite ocurre un error de desbordamiento (overflow).
Complementa un poco lo que mencionó el profesor en el video.
Miguel Torres

Miguel Torres

Profe Platzihace 3 años

Así es, en python el límite de recursividad es 1000.

En los siguientes cursos de esta ruta verás más sobre ello y verán cómo modificar ese límite con un módulo de python llamadoos y cuándo debería hacerse. 😉
"""