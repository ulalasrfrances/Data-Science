from time import time #importamos la función time para capturar tiempos
 
lista =list(range(0,40)) #vector de valores desde 0 a 99
 
tiempo_inicial = time() 
 
for i in lista:
    print(i)
 
tiempo_final = time() 
 
tiempo_ejecucion = tiempo_final - tiempo_inicial
 
print( 'El tiempo de ejecucion fue:',tiempo_ejecucion) #En segundos