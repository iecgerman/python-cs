"""num_1 = int(input('Escoge un número: '))
num_2 = int(input('Escoge otro número: '))

if num_1 > num_2:
    print('El primer número es mayor que el segundo número')

elif num_1 < num_2:
    print('El segundo número es mayor que el primer número')

else:
    print('Los dos números son iguales')"""

# RETO

user1 = input('¿Cual es el nombre del primer usuario? ')

edad1 = int(input('¿Que edad tiene el primer usuario? '))

user2 = input('¿Cual es el nombre del segundo usuario? ')

edad2 = int(input('¿Que edad tiene el segundo usuario? '))

if edad1 > edad2:
    print(f'{user1} tiene {edad1} años y es mayor que {user2} que tiene {edad2} años.')

elif edad1 < edad2:
    print(f'{user1} tiene {edad1} años y es menor que {user2} que tiene {edad2} años.')

else:
    print(f'{user1} tiene {edad1} años y tiene la misma edad que {user2} que tiene {edad2} años.')

