import time
start_time = time.time()
objetivo = int(input('Escoge un numero: '))
epsilon = 0.001
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2
num = 0 #numero para contar iteraciones
start = time.time()
# la funcion absolute value para encontrar valores abosolutos
while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta

    respuesta = (alto + bajo) / 2

    num += 1

end = time.time()

print(f'La raiz cuadrada de {objetivo} es {respuesta}')
print("--- %s seconds ---" % (time.time() - start_time))
print(f'Para resolver hizo {num} iteraciones y se demoro {end - start} segundos')
