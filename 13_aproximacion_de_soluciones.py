import time
start_time = time.time()

# número al que se calculará la raiz cuadrada
objetivo = int(input('Escoge un número: '))

# margen de error para encontrar esa raiz cuadrada
epsilon = 0.01

# valor que se irá sumando secuecuencialmente hasta encontrar la raiz cuadrada
paso = epsilon**2

# se comenzara a buscar a la raiz cuadrada desde 0.0 en adelante
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')

else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

print("--- %s seconds ---" % (time.time() - start_time))