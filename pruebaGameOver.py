import pygame

def gameOver():
    font.init
    font=pygame.font.Font(None,50)
    mensajeGameOver = font.render("SACABAO L'JUEGO, YA LO SIENTO", 1, (255,255,255))
    pantalla.blit(mensajeGameOver, (110, 300))
    pygame.time.delay(1000)

gameOver()