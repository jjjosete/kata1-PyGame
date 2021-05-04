import pygame as pg
import sys
from random import randint, choice

ROJO = (255, 0,0)
VERDE = (0, 255, 0)
AZUL =(0, 0, 255)
NEGRO =(0, 0, 0)
newValues = list(range(-10, -4)) + list(range(5, 11))
ANCHO = 800
ALTO = 600

pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))

class Bola():
    def __init__(self, x, y, vx, vy, color, radio = 7):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.altura = radio*2
        self.anchura = radio*2


    def actualizar(self):
 
        self.x += self.vx
        self.y += self.vy

        if  self.x <= 0 or self.x>= ANCHO:
            self.vx = -self.vx

        if  self.y <= 0 :
            self.vy = -self.vy

        if  self.y>= ALTO:
            self.x =ANCHO //2
            self.y =ALTO //2
            self.vx = choice(newValues)
            self.vy = choice(newValues)

            return -1
        return 0

    def dibujar(self, lienzo):
        pg.draw.circle(lienzo, self.color, (self.x, self.y), self.anchura//2)
    
    def compruebaColision(self, objeto):
        choqueX = self.x >= objeto.x and self.x <= objeto.x + objeto.anchura or \
        self.x + self.anchura >= objeto.x and self.x+self.anchura <= objeto.x + objeto.anchura

        choqueY = self.y >= objeto.y and self.y <= objeto.y + objeto.altura or \
        self.y + self.altura >= objeto.y and self.y+self.altura <= objeto.y + objeto.altura

        if choqueX and choqueY:
            self.vy *=-1 
           

class Raqueta():
        def __init__(self):
            self.altura = 25
            self.anchura = 100
            self.color = (255, 255, 255)
            self.x = (ANCHO- self.anchura) // 2
            self.y = ALTO - self.altura - 15
            self.vy = 0
            self.vx = 13

        def dibujar(self, lienzo):
            rect = pg.Rect(self.x, self.y, self.anchura, self.altura)
            pg.draw.rect(lienzo, self.color, rect)
            
        def actualizar(self):   
            teclas_pulsadas=pg.key.get_pressed()
            if teclas_pulsadas[pg.K_LEFT] and self.x > 0:
                self.x -= self.vx

            if teclas_pulsadas[pg.K_RIGHT] and self.x < ANCHO - self.anchura:
                self.x += self.vx
def gameOver():
    
    

vidas = 3

bola = Bola(randint(0, ANCHO),
            randint(0, ALTO),
            choice(newValues),
            choice(newValues),
            (randint(0, 255), randint(0, 255), randint(0, 255)))
                

raqueta = Raqueta()                

game_over = False

reloj = pg.time.Clock()

while not game_over and vidas > 0:
    reloj.tick(60)
    #Gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

   #gestion de estado
    raqueta.actualizar()
    pierdebola = bola.actualizar()
    if pierdebola:
        vidas-= 1
    bola.compruebaColision(raqueta)
    
    #gestion de pantalla
    pantalla.fill(NEGRO)
    bola.dibujar(pantalla)    
    raqueta.dibujar(pantalla)
        
    pg.display.flip()
    if pierdebola:
        pg.time.delay(500)

pg.quit()
sys.exit()
