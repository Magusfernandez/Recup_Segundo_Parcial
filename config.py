import pygame


ANCHO_VENTANA = 900
ALTO_VENTANA = 650

ancho_boton = 200
alto_boton = 70

dificultad = 10  # Dificultad inicial: fácil
tablero_oculto = []
estado_casillas = []
tam_celda = 40
pos_centrado = (0, 0)

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

#COLOR_FONDO = (20, 50, 153)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
#GRIS = (70,70,70)
AZUL = (34, 69, 179)
ROJO = (231, 30, 30)

