import pygame
import random
from config import *
AZUL = (34, 69, 179)


pygame.init()

def inicializar_tablero(dificultad:int)->list:
    '''
    Inicializa una matriz vacia y la retorna.
    '''
    matriz = []
    for _ in range(dificultad):
        fila = [0] * dificultad
        matriz += [fila] 

    return matriz

def mostrar_matriz(matriz:list)->None:
    '''
    Funcion: mostrar una matriz 
    Parametro: recibe por parametro una matriz y la muestra
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],  end=" ")
        print("")


def colocar_navio(matriz:list, tipo_navio:str, cantidad:int):
    """
    Recibe una matriz, un tipo de navio (submarino, destructor, crucero o acorazado)
    y la cantidad de navios que se quiere colocar.
    """

    match tipo_navio:
        case "submarino":
            largo = 1
        case "destructor":
            largo = 2
        case "crucero":
            largo = 3
        case "acorazado":
            largo = 4

    contador_colocados = 0

    while contador_colocados < cantidad:

        fila_inicial = random.randint(0, len(matriz) - (largo))
        columna_inicial = random.randint(0, len(matriz[0]) - (largo))
        orientacion = random.choice(["H", "V"])

        if validar_casilleros(matriz, fila_inicial, columna_inicial, largo, orientacion) == True:
            contador_colocados += 1
            for _ in range(largo):

                matriz[fila_inicial][columna_inicial] = largo

                if orientacion == "H":
                    columna_inicial += 1
                else:
                    fila_inicial += 1
    
def validar_casilleros(matriz:list,fila:int, columna:int, largo:int, orientacion:str):
    """
    recibe una matriz, una fila, una columna, el largo del objeto que se quiere colocar
    y la orientacion del objeto ("H"/"V")
    verifica que todos los espacios necesarios sean del valor 0 y devuelve true.
    si algun casillero es distinto a 0 devuelve false.
    """
    bandera_vacio = True
    contador = 0
    if orientacion == "H" and (columna + largo) < len(matriz[0]):
        while contador < largo:
            if matriz[fila][columna] != 0:
                bandera_vacio = False
                break

            columna += 1
            contador += 1

    if orientacion == "V" and (fila + largo) < len(matriz):
        while contador < largo:
            if matriz[fila][columna] != 0:
                bandera_vacio = False
                break

            fila += 1
            contador += 1
    
    return bandera_vacio


def dibujar_tablero(ventana, tablero_oculto, estado_casillas, tam_celda, pos_centrado):
    """
    Dibuja un tablero que representa una matriz
    Recibe como parametros la ventana donde sera creado el tablero, la matriz que sera oculta, la matriz visual,
    el tamaño de la celda y la posicion centrada del tablero.
    Retorna la matriz de rectangulos.
    """

    matriz_rectangulos = []
    for fila in range(len(tablero_oculto)):
        fila_rectangulos = []
        for columna in range(len(tablero_oculto[fila])):
            
            x = pos_centrado[0] + columna * tam_celda
            y = pos_centrado[1] + fila * tam_celda

            if estado_casillas[fila][columna] == 0: 
                color = NEGRO
            elif estado_casillas[fila][columna] == -1:  
                color = AZUL
            elif estado_casillas[fila][columna] == 1: 
                color = (255, 255, 0)  
            elif estado_casillas[fila][columna] == 2:  
                color = ROJO


            rect = pygame.draw.rect(ventana, color, (x, y, tam_celda - 2, tam_celda - 2))
            fila_rectangulos.append(rect)

        matriz_rectangulos.append(fila_rectangulos)

    return matriz_rectangulos


def nave_hundida(tablero_oculto, tipo_nave):
    """
    Verifica si una nave está completamente hundida.
    Recibe como parametros el tablero oculto (matriz logica con las naves), y el tipo de nave.
    Retorna True si la nave esta completamente hundida, de lo contrario retorna False.
    """
    for fila in tablero_oculto:
        if tipo_nave in fila: 
            return False
    return True

def contar_casillas_nave(tablero_oculto, tipo_nave):
    """
    Cuenta cuántas casillas ocupa una nave en el tablero.
    Recibe por parametro el tablero oculto con la matriz logica de las naves y 
    el tipo de nave (el numero que representa cada nave).
    Retorna el numero total de casillas que ocupa la nave.
    """
    contador = 0
    for fila in tablero_oculto:
        contador += fila.count(tipo_nave) 
    return contador

def actualiza_y_dibuja_tablero(ventana, dificultad):
    """
    Crea y dibuja el tablero para el nivel de dificultad indicado.
    Calcula el tamaño de las celdas y posiciones para centrar el tablero.
    Devuelve una matriz de rectángulos interactivos.
    """
    
    tam_celda = {10: 40, 20: 30, 40: 15}[dificultad]
    cantidad_filas_columnas = dificultad
    ancho_tablero = tam_celda * cantidad_filas_columnas
    alto_tablero = tam_celda * cantidad_filas_columnas
    pos_centrado = ((ANCHO_VENTANA - ancho_tablero) // 2, (ALTO_VENTANA - alto_tablero) // 2)

    
    tablero_oculto = inicializar_tablero(cantidad_filas_columnas)
    estado_casillas = inicializar_tablero(cantidad_filas_columnas)

    # Colocar naves
    multiplicador_naves = {10: 1, 20: 2, 40: 3}[dificultad]
    colocar_navio(tablero_oculto, "submarino", 4 * multiplicador_naves)
    colocar_navio(tablero_oculto, "destructor", 3 * multiplicador_naves)
    colocar_navio(tablero_oculto, "crucero", 2 * multiplicador_naves)
    colocar_navio(tablero_oculto, "acorazado", 1 * multiplicador_naves)

    matriz_rectangulos = dibujar_tablero(ventana, tablero_oculto, estado_casillas, tam_celda, pos_centrado)


    return matriz_rectangulos, tablero_oculto, estado_casillas


def procesar_disparo(fila, columna, puntaje, tablero_oculto, estado_casillas):
    """
    Procesa un disparo en la posición indicada.
    Actualiza el estado de las matrices y el puntaje según el resultado.
    """
    if estado_casillas[fila][columna] != 0:
        print("Casilla ya disparada.")
        return puntaje, estado_casillas

    if tablero_oculto[fila][columna] == 0:  # Agua
        estado_casillas[fila][columna] = -1
        puntaje -= 1
    else:  # Parte de una nave
        tipo_nave = tablero_oculto[fila][columna]

        tablero_oculto[fila][columna] = -1  # Marcar como impactada
        if nave_hundida(tablero_oculto, tipo_nave):
            estado_casillas[fila][columna] = 2  # Nave hundida
            tamano = contar_casillas_nave(tablero_oculto, tipo_nave)
            puntaje += tamano * 10
        else:
            estado_casillas[fila][columna] = 1  # Nave dañada
            puntaje += 5

    return puntaje, estado_casillas


def detectar_click(pos_mouse, matriz_rectangulos, tablero_oculto, estado_casillas):
    """
    Detecta clics sobre el tablero y actualiza el estado de la celda correspondiente.
    Pinta azul para agua, amarillo/naranja para nave golpeada, y rojo para nave hundida.
    """
    for i in range(len(matriz_rectangulos)): 
        for j in range(len(matriz_rectangulos[i])): 
            rect = matriz_rectangulos[i][j] 
            if rect.collidepoint(pos_mouse):  
               
                if tablero_oculto[i][j] == 0:
                    estado_casillas[i][j] = -1
               
                elif tablero_oculto[i][j] > 0:
                    
                    tipo_nave = tablero_oculto[i][j]
                    if nave_hundida(tablero_oculto, tipo_nave) == True: 
                        estado_casillas[i][j] = 2
                    else: 
                        estado_casillas[i][j] = 1
    return estado_casillas  
