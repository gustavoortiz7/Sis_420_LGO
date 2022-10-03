import random

def crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios):
# Se crea un mapa lleno de paredes
    mapa_laberinto = []
    numero_paredes_generadas = 0
    for fila in range(0, numero_filas):
        fila_mapa_laberinto = []
        for columna in range(0, numero_columnas):
#             if (random.randrange(2) == 1 and numero_paredes_generadas < numero_paredes):
#                 fila_mapa_laberinto.append('#')
#                 numero_paredes_generadas += 1
#             else:
#                 fila_mapa_laberinto.append(' ')
            fila_mapa_laberinto.append('#')
        mapa_laberinto.append(fila_mapa_laberinto)
        
#Se ubica aleatoriamente un punto de inicio y a partir de ese punto se llenan espacios
    numero_espacios_generados = 0
    fila_posicion_actual = random.randrange(numero_filas)
    #print("fila",fila_posicion_actual)
    columna_posicion_actual = random.randrange(numero_columnas)
    #print("columna",columna_posicion_actual)
    mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
    numero_espacios_generados += 1

#Se ubica una ficha con la fila actual y columna actual
    #ficha_fila = random.randrange(numero_filas)
    #ficha_columnas = random.randrange(numero_columnas)
    mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = 'P'

    while numero_espacios_generados < numero_espacios:
        direccion = random.randrange(4)
        if direccion == 0 and fila_posicion_actual > 0:
            fila_posicion_actual -= 1
        elif direccion == 1 and fila_posicion_actual < numero_filas - 1:
            fila_posicion_actual += 1
        elif direccion == 2 and columna_posicion_actual > 0:
            columna_posicion_actual -= 1
        else:
            if columna_posicion_actual < numero_columnas - 1:
                columna_posicion_actual += 1
            
        if mapa_laberinto[fila_posicion_actual][columna_posicion_actual] == '#':
            mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
            numero_espacios_generados += 1
            
    return mapa_laberinto


numero_filas = int(input('Introduzca el número de filas : '))
numero_columnas = int(input('Introduzca el número de columnas : '))
numero_paredes = int(input('Introduzca el número de paredes : '))
numero_espacios = numero_filas * numero_columnas - numero_paredes
espacios_aleatorios = int(input('Introduzca los espacios aleatorio que se desplazara : '))
print("Las filas son:",numero_filas)
print("Las columnas son:",numero_columnas)
print("Las paredes son:",numero_paredes)
print("Las espacios son:",numero_espacios)

laberinto = crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios)

#def hayespacio (laberinto,numerofilas,numerocolumnas):
 #   numeroespacios=0;
#
 #   if numerofilas > 0 and laberinto[numerofilas-1][numerocolumnas]== " ":
 #       numeroespacios +=1
 #   if numerofilas < len(laberinto) and laberinto[numerofilas+1][numerocolumnas]== " ":
 #       numeroespacios+=1
 #   if numerocolumnas > 0 and laberinto[numerofilas][numerocolumnas-1]== " ":
 #       numeroespacios +=1
 #   if numerocolumnas < len(laberinto[0][:]) and laberinto[numerofilas][numerocolumnas+1]== " ":
 #       numeroespacios+=1
        
 #   if numeroespacios >0:
  #      return True
  #  else:
   #     return False


for fila_mapa_laberinto in laberinto:
    print(fila_mapa_laberinto)


print("Los espacios aleatorios avanzados son")
cont =0
while cont < espacios_aleatorios:
    ficha_fila = random.randrange(numero_filas)
    ficha_columas = random.randrange(numero_columnas)
    if laberinto[ficha_fila][ficha_columas] == ' ':
        laberinto[ficha_fila][ficha_columas] = 'P'
        cont +=1
        for fila_mapa_laberinto in laberinto:
            print(fila_mapa_laberinto)
        print("  ")
print("Ya se desplazaron todos ")
