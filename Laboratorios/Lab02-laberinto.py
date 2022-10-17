import random

numero_filas = int(input("introducir numero de filas: "))
numero_columnas = int(input("introducir numero de columnas: "))
#numero_paredes = int(input("introducir numero de paredes: "))
laberinto =[]
#mostrar laberinto
def mostrar (laberinto):
    for filas in laberinto:
        for valor in filas:
            print( valor, end=" ")
        print()

#marcos laberinto
for i in range(0,numero_filas):
    fila=[]   
    for j in range(0,numero_columnas):         
        if i == 0 or j==0 or i == numero_filas -1 or j == numero_columnas -1 :
            fila.append('#')
        else: 
            fila.append(0)
    laberinto.append(fila)

#laberinto
numero_paredes = int((numero_columnas+numero_filas)/2)
for p in range(numero_paredes*4):
    fila_actual =random.randrange(2,numero_filas-2)
    columna_actual=random.randrange(2,numero_columnas-2)
    #evita paredes dobles
    fila_actual = int((fila_actual / 2)) * 2
    columna_actual = int((columna_actual / 2)) * 2 
   
    laberinto[fila_actual][columna_actual] = '#'
    if laberinto[fila_actual][columna_actual-2] == 0:
        laberinto[fila_actual][columna_actual-2] = '#'
        laberinto[fila_actual][columna_actual-1] = '#'
    if laberinto[fila_actual][columna_actual+2] == 0:
        laberinto[fila_actual][columna_actual+2] = '#'
        laberinto[fila_actual][columna_actual+1] = '#'
    if laberinto[fila_actual-2][columna_actual] == 0:
        laberinto[fila_actual-2][columna_actual] = '#'
        laberinto[fila_actual-1][columna_actual] = '#'
    if laberinto[fila_actual+2][columna_actual] == 0:
        laberinto[fila_actual+2][columna_actual] = '#'
        laberinto[fila_actual+1][columna_actual] = '#'

#generador de personas
contador_personas = 0
personas_pos =[]
while True:
    persona_f =random.randrange(1,numero_filas-1)
    persona_c=random.randrange(1,numero_columnas-1)
    if laberinto[persona_f][persona_c] == 0:
        laberinto[persona_f][persona_c] = "*"
        contador_personas += 1
        personas_pos.append(persona_f)  
        personas_pos.append(persona_c)
    if len(personas_pos) == 6:
        break
#eliminar los 0
for i in range(0,numero_filas):
    for j in range(0,numero_columnas):
        if laberinto[i][j]==0:
            laberinto[i][j]=" "
#buscador de personas
    #(ordenando el array de las posisiones de las personas)
personas_pos_ord =[]
if personas_pos[0]+personas_pos[1] < personas_pos[2]+personas_pos[3] and personas_pos[0]+personas_pos[1] < personas_pos[4]+personas_pos[5] :
    personas_pos_ord.append(personas_pos[0])
    personas_pos_ord.append(personas_pos[1])
    if personas_pos[2]+personas_pos[3] < personas_pos[4]+personas_pos[5]:
        personas_pos_ord.append(personas_pos[2])
        personas_pos_ord.append(personas_pos[3])
        personas_pos_ord.append(personas_pos[4])
        personas_pos_ord.append(personas_pos[5])
    else:
        personas_pos_ord.append(personas_pos[4])
        personas_pos_ord.append(personas_pos[5])
        personas_pos_ord.append(personas_pos[2])
        personas_pos_ord.append(personas_pos[3])
elif personas_pos[2]+personas_pos[3] < personas_pos[0]+personas_pos[1] and personas_pos[2]+personas_pos[3] < personas_pos[4]+personas_pos[5] :
    personas_pos_ord.append(personas_pos[2])
    personas_pos_ord.append(personas_pos[3])
    if personas_pos[0]+personas_pos[1] < personas_pos[4]+personas_pos[5]:
        personas_pos_ord.append(personas_pos[0])
        personas_pos_ord.append(personas_pos[1])
        personas_pos_ord.append(personas_pos[4])
        personas_pos_ord.append(personas_pos[5])
    else:
        personas_pos_ord.append(personas_pos[4])
        personas_pos_ord.append(personas_pos[5])
        personas_pos_ord.append(personas_pos[0])
        personas_pos_ord.append(personas_pos[1])
else:
    personas_pos_ord.append(personas_pos[4])
    personas_pos_ord.append(personas_pos[5])
    if personas_pos[0]+personas_pos[1] < personas_pos[2]+personas_pos[3]:
        personas_pos_ord.append(personas_pos[0])
        personas_pos_ord.append(personas_pos[1])
        personas_pos_ord.append(personas_pos[2])
        personas_pos_ord.append(personas_pos[3])
    else:
        personas_pos_ord.append(personas_pos[2])
        personas_pos_ord.append(personas_pos[3])
        personas_pos_ord.append(personas_pos[0])
        personas_pos_ord.append(personas_pos[1])
    #buscador
laberinto[1][1]= "-"
fi=1
co=1
def encontrado():   
    if laberinto[fi+1][co] == "*" or laberinto[fi][co+1] == "*" or laberinto[fi][co-1] == "*" or laberinto[fi-1][co] == "*":
        print ("SE A ENCONTRADO A UNA PERSONA")
        return True
    return False

while True:
    #encontrado()
    if personas_pos_ord[0] > personas_pos_ord[1]:
        #posicionandose en el eje Y
        for i in range(1,personas_pos_ord[0]):    
            if laberinto[fi+1][co] == " ":
                laberinto[fi+1][co]= "-"
                fi+=1
        if encontrado()==True:
            print ("posision f: ",fi," posision c: ",co)
            break           
        #buscando camino eje X
        if laberinto[fi][co+1] == " ":
            for i in range(1,personas_pos_ord[1]):
                if laberinto[fi][co+1] == " ":
                    laberinto[fi][co+1]= "-"
                    co+=1
        if encontrado()==True:
            print ("posision f: ",fi," posision c: ",co)
            break            
        for i in range(1,4):
            if laberinto[fi+i][co+1] == " ":
                laberinto[fi+i][co+1] = "-"
                co+=i
                fi+=i
                break    
            elif laberinto[fi-i][co+1] == " ":
                laberinto[fi-i][co+1] = "-"
                co+=i
                fi-=i
                break
        encontrado()
        #print ("posision f: ",fi," posision c: ",co)

    else:
        for i in range(1,personas_pos_ord[1]):               
            if laberinto[fi][co+1] == " ":
                laberinto[fi][co+1]= "-"
                co+=1
        if laberinto[fi+1][co] == " ":
            for i in range(1,personas_pos_ord[0]):    
                if laberinto[fi+1][co] == " ":
                    laberinto[fi+1][co]= "-"
                    fi+=1
        encontrado()
        print ("posision f: ",fi," posision c: ",co)       
    break
#mostrar laberinto
mostrar (laberinto)
print("SE GENERARON ",contador_personas," PERSONAS")
print("posisiones generadas: ",personas_pos)
print("posisiones ordenadas: ",personas_pos_ord)

