"""
>>> my_dict = {
...     'David': 35,
...     'Erika': 32,
...     'Jaime': 50,
... }
>>> 
>>> my_dict['David']
35
>>> my_dict['Erik']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Erik'
>>> my_dict.get('Juan', 30)
30
>>> my_dict.get('David', 30)
35
>>> my_dict['Jaime'] = 20
>>> my_dict
{'David': 35, 'Erika': 32, 'Jaime': 20}
>>> my_dict['Pedro'] = 70
>>> my_dict
{'David': 35, 'Erika': 32, 'Jaime': 20, 'Pedro': 70}
>>> 
>>> 
>>> del my_dict['Jaime']
>>> my_dict
{'David': 35, 'Erika': 32, 'Pedro': 70}
>>> 
>>> 

>>> for llave in  my_dict.keys():
...     print(llave)
... 
David
Erika
Pedro
>>> 

>>> my_dict = {
...     'David': 35,
...     'Erika': 32,
...     'Jaime': 50,
... }
>>> my_dict
{'David': 35, 'Erika': 32, 'Jaime': 50}
>>> for valor in my_dict.values():
...     print(valor)
... 
35
32
50
>>> for llave, valor in my_dict.items():
...     print(llave, valor)
... 
David 35
Erika 32
Jaime 50
>>> 
>>> 'David' in my_dict
True
>>> 'German' in my_dict
False
>>> 



"""