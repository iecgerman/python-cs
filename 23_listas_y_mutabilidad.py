"""
Acá investigue los métodos de listas: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

Los nuevos que encontré además de los de la clase:

    lista.extend(iterable) #extiende la lista con valores dentro de un iterable como un range()
    lista.insert(i, ‘valor’) #Agrega un valor en la posición i y recorre todos los demás. No borra nada.
    lista.pop(i) #Elimina valor en la posición i de la lista.
    lista.remove(‘valor’) #Elimina el primer elemento con ese valor.
    lista.clear() #Borra elementos en la lista.
    lista.index(‘valor’) #Retorna posición del primer elemento con el valor.
    lista.index(‘valor’, start, end) #Retorna posición del elemento con el valor dentro de los elementos desde posición start hasta posición end)
    lista.count(‘valor’) #Cuenta cuántas veces esta ese valor en la lista.
    lista.sort() #Ordena los elementos de mayor a menor.
    lista.sort(reverse = True) #Ordena los elementos de menor a mayor.
    lista.reverse() #Invierte los elementos
    lista.copy() #Genera una copia de la lista. También útil para clonar listas.

"""

"""
>>> my_list = [1,2,3]
>>> my_list[0]
1
>>> my_list[1:]
[2, 3]
>>> 
>>> my_list.append(4)
>>> print(my_list)
[1, 2, 3, 4]
>>> 
>>> my_list[0] = 'a'
>>> print(my_list)
['a', 2, 3, 4]
>>> my_list.pop()
4
>>> print(my_list)
['a', 2, 3]
>>> 
>>> 
>>> for element in my_list:
...     print(element)
... 
a
2
3
>>> 
>>> a = [1,2,3]
>>> b = a
>>> 
>>> a
[1, 2, 3]
>>> b
[1, 2, 3]
>>> id(a)
140187644239936
>>> id(b)
140187644239936
>>> 
>>> c = [a,b]
>>> c
[[1, 2, 3], [1, 2, 3]]
>>> 
>>> a.append(5)
>>> a
[1, 2, 3, 5]
>>> c
[[1, 2, 3, 5], [1, 2, 3, 5]]
>>> 
>>> 
>>> 
>>> 
>>> a = [1,2,3]
>>> id(a)
140187644242368
>>> b = a
>>> id(b)
140187644242368
>>> 
>>> c = list(a)
>>> a
[1, 2, 3]
>>> b
[1, 2, 3]
>>> c
[1, 2, 3]
>>> id(a)
140187644242368
>>> id(c)
140187644396224
>>> 
>>> d = a[::]
>>> print(d)
[1, 2, 3]
>>> id(d)
140187644227584
>>> 
>>> 
>>> my_list = list(range(100))
>>> my_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>>  
>>> double = [ i * 2 for i in my_list]
>>> double
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198]
>>> 
>>> pares = [ i for i in my_list if i % 2 == 0]
>>> pares
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> 

"""