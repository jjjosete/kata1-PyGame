import pygame as pg
import sys
from random import randint, choice

def tocaBorde():
    if bola.x  <= bounds.left or bola.x >= bounds.right:
        bola.vx *= -1 
    if bola.y <= bounds.top or bola.y >= bounds.bottom:
        bola.vy *= -1 

ROJO = (255, 0,0)
VERDE = (0, 255, 0)
AZUL =(0, 0, 255)
NEGRO =(0, 0, 0)
newValues = list(range(-10, -4)) + list(range(5, 11))
ANCHO = 800
ALTO = 600
bounds = pg.Rect(20, 20, 760, 560) #Creacion del borde

pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))

class Bola():
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color



bolas = []
for i in range(10):
    bola = Bola(randint(0, ANCHO),
                randint(0, ALTO),
                choice(newValues),
                choice(newValues),
                (randint(0, 255), randint(0, 255), randint(0, 255)))
    

    bolas.append(bola)

game_over = False

reloj = pg.time.Clock()

while not game_over:
    reloj.tick(60)
    #Gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    for bola in bolas:
        bola.x += bola.vx
        bola.y += bola.vy

   
    


    pantalla.fill(NEGRO)
    pg.draw.rect(pantalla, ROJO, bounds,1)
    for bola in bolas:
        tocaBorde()
        pg.draw.circle(pantalla, bola.color, (bola.x, bola.y), 10)
        
    pg.display.flip()

pg.quit()
sys.exit()