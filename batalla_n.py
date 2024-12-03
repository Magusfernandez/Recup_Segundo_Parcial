import pygame
from funcion_batalla import *
from config import *
import pygame.mixer as mixer


pygame.init()
pygame.mixer.init()

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
mixer.music.load("juego_b_naval.py\musica_fondo.mp3")
mixer.music.play()
ruido_bomba = mixer.Sound("juego_b_naval.py\\efecto_bomba.mp3")
ruido_bomba.set_volume(0.5)

icono = pygame.image.load("juego_b_naval.py\\logo3.jpg")
pygame.display.set_icon(icono)

pygame.display.set_caption("Batalla Naval")

fondo_principal = pygame.image.load("juego_b_naval.py\\fondo1.jpg")
fondo_principal = pygame.transform.scale(fondo_principal, (ANCHO_VENTANA, ALTO_VENTANA))

fondo = pygame.image.load("juego_b_naval.py\\fondo2.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

fondo_puntajes = pygame.image.load("juego_b_naval.py\\fondo.jpg")
fondo_puntajes = pygame.transform.scale(fondo_puntajes, (ANCHO_VENTANA, ALTO_VENTANA))

fuente_puntos = pygame.font.SysFont("Consola", 25, bold = False)




imagen_nivel = pygame.image.load("juego_b_naval.py\\nivel.png")
imagen_jugar = pygame.image.load("juego_b_naval.py\\jugar.png")
imagen_puntaje = pygame.image.load("juego_b_naval.py\\ver_puntaje.png")
imagen_salir = pygame.image.load("juego_b_naval.py\\salir.png")
imagen_reiniciar = pygame.image.load("juego_b_naval.py\\reiniciar.png")
imagen_volver = pygame.image.load("juego_b_naval.py\\volver.png")
imagen_facil = pygame.image.load("juego_b_naval.py\\facil.png")
imagen_medio = pygame.image.load("juego_b_naval.py\\medio.png")
imagen_dificil = pygame.image.load("juego_b_naval.py\dificil.png")
#imagen_guardar = pygame.image.load("juego_b_naval.py\\guardar.png")

imagen_puntos = pygame.image.load("juego_b_naval.py\\fondo_boton.png")

imagen_nivel = pygame.transform.scale(imagen_nivel, (ancho_boton, alto_boton))
imagen_jugar = pygame.transform.scale(imagen_jugar, (ancho_boton, alto_boton))
imagen_puntaje = pygame.transform.scale(imagen_puntaje, (ancho_boton, alto_boton))
imagen_salir = pygame.transform.scale(imagen_salir, (ancho_boton, alto_boton))
imagen_reiniciar = pygame.transform.scale(imagen_reiniciar, (ancho_boton - 60, alto_boton - 20))
imagen_volver = pygame.transform.scale(imagen_volver, (ancho_boton - 60, alto_boton - 20))
imagen_facil = pygame.transform.scale(imagen_facil, (ancho_boton, alto_boton))
imagen_medio = pygame.transform.scale(imagen_medio, (ancho_boton, alto_boton))
imagen_dificil = pygame.transform.scale(imagen_dificil, (ancho_boton, alto_boton))
imagen_puntos = pygame.transform.scale(imagen_puntos, (ancho_boton - 70, alto_boton))
#imagen_guardar = pygame.transform.scale(imagen_guardar, (ancho_boton - 60, alto_boton - 20))

boton_jugar = imagen_jugar.get_rect()
boton_jugar.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_jugar.y = (ALTO_VENTANA / 6)

boton_nivel = imagen_nivel.get_rect()
boton_nivel.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_nivel.y = (ALTO_VENTANA / 3)

boton_puntaje = imagen_puntaje.get_rect()
boton_puntaje.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_puntaje.y = (ALTO_VENTANA / 2)

boton_salir = imagen_salir.get_rect()
boton_salir.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_salir.y = (ALTO_VENTANA - ALTO_VENTANA / 3)

boton_volver = imagen_reiniciar.get_rect()
boton_volver.x = 755
boton_volver.y = 590

# boton_guardar = imagen_guardar.get.rect()
# boton_guardar.x = 10
# boton_guardar.y = 590

boton_reiniciar = imagen_reiniciar.get_rect()
boton_reiniciar.x = 3
boton_reiniciar.y = 590

boton_facil = imagen_facil.get_rect()
boton_facil.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_facil.y = (ALTO_VENTANA / 6)

boton_medio = imagen_medio.get_rect()
boton_medio.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_medio.y = (ALTO_VENTANA / 3)

boton_dificil = imagen_dificil.get_rect()
boton_dificil.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_dificil.y = (ALTO_VENTANA / 2)


bandera_pantallas = 0
puntos = 0
dificultad = 10
matriz_rectangulos = []
tablero_oculto = []
estado_casillas = []

corriendo = True

while corriendo == True:

    if bandera_pantallas == 0:
        mixer.music.set_volume(10)
        ventana.blit(fondo_principal, (0, 0))
        ventana.blit(imagen_jugar, boton_jugar)
        ventana.blit(imagen_nivel, boton_nivel)
        ventana.blit(imagen_puntaje, boton_puntaje)
        ventana.blit(imagen_salir, boton_salir)
        

    elif bandera_pantallas == 1:       
        if not matriz_rectangulos:
            matriz_rectangulos, tablero_oculto, estado_casillas = actualiza_y_dibuja_tablero(ventana, dificultad)
        ventana.blit(fondo, (0, 0))
        ventana.blit(imagen_reiniciar, boton_reiniciar)
        ventana.blit(imagen_volver, boton_volver)
        #ventana.blit(imagen_guardar, boton_guardar)
        texto_puntos = fuente_puntos.render(f"Puntos: {str(puntos)}", True, BLANCO, None)
        ancho_texto_puntos = texto_puntos.get_size()[0] 
        ventana.blit(imagen_puntos, (5, 5))
        ventana.blit(texto_puntos, (15, 20))
        
        matriz_rectangulos = dibujar_tablero(ventana, tablero_oculto, estado_casillas, tam_celda, pos_centrado)

       
    elif bandera_pantallas == 2:   
        ventana.blit(fondo_puntajes, (0, 0))
        ventana.blit(imagen_volver, boton_volver)


    elif bandera_pantallas == 3:    
        ventana.blit(fondo_puntajes, (0, 0))
        ventana.blit(imagen_facil, boton_facil)
        ventana.blit(imagen_medio, boton_medio)
        ventana.blit(imagen_dificil, boton_dificil)
        ventana.blit(imagen_volver, boton_volver)
            

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                corriendo = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()
           

            if bandera_pantallas == 0:
                if boton_salir.collidepoint(pos_mouse):
                    corriendo = False

                elif boton_jugar.collidepoint(pos_mouse):
                    bandera_pantallas = 1 
                   
                
                elif boton_nivel.collidepoint(pos_mouse):
                    bandera_pantallas = 3
                    
                elif boton_puntaje.collidepoint(pos_mouse):
                    bandera_pantallas = 2
                

            elif bandera_pantallas == 1:

                for i in range(len(matriz_rectangulos)):  
                    for j in range(len(matriz_rectangulos[i])): 
                        rect = matriz_rectangulos[i][j]
                        if rect.collidepoint(pos_mouse):  
                                    
                            puntos, estado_casillas = procesar_disparo(i, j, puntos, tablero_oculto, estado_casillas)


                if boton_reiniciar.collidepoint(pos_mouse): 
                    matriz_rectangulos, tablero_oculto, estado_casillas = actualiza_y_dibuja_tablero(ventana, dificultad)
                    puntos = 0
                             
                
                elif boton_volver.collidepoint(pos_mouse):
                    bandera_pantallas = 0

                
            elif bandera_pantallas == 2:
                if boton_volver.collidepoint(pos_mouse):
                    bandera_pantallas = 0
            
            elif bandera_pantallas == 3:
                if boton_facil.collidepoint(pos_mouse):
                    dificultad = 10
                    matriz_rectangulos, tablero_oculto, estado_casillas = actualiza_y_dibuja_tablero(ventana, dificultad)
                    bandera_pantallas = 0
                elif boton_medio.collidepoint(pos_mouse):
                    dificultad = 20
                    matriz_rectangulos, tablero_oculto, estado_casillas = actualiza_y_dibuja_tablero(ventana, dificultad)
                    bandera_pantallas = 0
                elif boton_dificil.collidepoint(pos_mouse):
                    dificultad = 40
                    matriz_rectangulos, tablero_oculto, estado_casillas = actualiza_y_dibuja_tablero(ventana, dificultad)
                    bandera_pantallas = 0
                 
                elif boton_volver.collidepoint(pos_mouse):
                    bandera_pantallas = 0


 
    pygame.display.flip()

pygame.quit()