import pygame
import os.path
import random

class Personaje(pygame.sprite.Sprite):
    def __init__ (self, vida, posicionx, posiciony, tipo_personaje):
        pygame.sprite.Sprite.__init__(self)
        self.vida = vida
        self.posicionx = posicionx
        self.posiciony = posiciony
        self.recarga = 12
        if tipo_personaje == True:
            self.imagenes = pygame.image.load(os.path.join('Images', 'Sprite.png'))
            imagen = self.imagenes.subsurface(pygame.Rect(99, 1, 13, 31))
            self.image = pygame.transform.scale(imagen, (50, 100))
            self.posicion_de_imagenes = [(4, 1, 13, 32),   #ar,0,1 
                                         (28, 1, 13, 32),  #ar,1,2
                                         (52, 1, 13, 32),  #ar,2,3
                                         (75, 1, 13, 32),  #ab,3,1
                                         (99, 1, 13, 32),  #ab,4,2
                                         (123, 1, 13, 32), #ab,5,3
                                         (146, 1, 16, 32), #iz,6,1
                                         (170, 1, 16, 32), #iz,7,2
                                         (194, 1, 16, 32), #iz,8,3
                                         (218, 1, 16, 32), #der,9,1
                                         (242, 1, 16, 32), #der,10,2
                                         (266, 1, 16, 32)  #der, 11,3
                                        ]
            self.posicion_estado = { 'arriba':'0',
                                    'abajo':'3',
                                    'izquierda':'6',
                                    'derecha':'9',
                                    'actual':'abajo'
                                    }
        else:
            self.imagenes = pygame.image.load(os.path.join('Images', 'Spriteenemigo.png'))
            imagen = self.imagenes.subsurface(pygame.Rect(30, 5 ,13, 32))
            self.image = pygame.transform.scale(imagen, (50,100))
            self.posicion_de_imagenes = [(6, 5, 13, 32),   #ab,0,1
                                        (30, 5, 13, 32),  #ab,1,2
                                        (54, 5, 13, 32),  #ab,2,3
                                        (101, 5, 15, 32), #iz,3,1
                                        (125, 5, 15, 32), #iz,4,2
                                        (149, 5, 15, 32), #iz,5,3
                                        (200, 5, 12, 32), #ar,6,1
                                        (224, 5, 12 ,32), #ar,7,2
                                        (248, 5, 12, 32), #ar,8,3
                                        (294, 5, 15, 32), #der,9,1
                                        (318, 5, 15, 32), #der,10,2
                                        (342, 5, 15, 32)  #der,11,3
                                       ]
            self.posicion_estado = { 'arriba':'6',
                                    'abajo':'0',
                                    'izquierda':'4',
                                    'derecha':'9',
                                    'actual':'abajo'
                                    }

        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.posicionx,self.posiciony)



class Enemigo(Personaje):
    def __init__ (self, vida, posicionx, posiciony, tipo_personaje):
        Personaje.__init__(self, vida, posicionx, posiciony, tipo_personaje)
        self.alerta = False
        self.disparando = False
        self.esperar = 15
        self.eleccion = random.randint(0,5)
        self.recarga = 7

    def accion(self, stalker, disparos,objetos):
        actual = self.posicion_estado.get('actual')
        if stalker.posicionx <= self.posicionx+24 <= stalker.posicionx+50:
            if actual == 'abajo' and stalker.posiciony >= self.posiciony+100:
                if self.recarga == 7:
                    pygame.mixer.music.play()
                    disparo = bala(self.posicionx, self.posiciony, actual)
                    disparos.add(disparo)
                    self.disparando = True
                    self.recarga = 0
            if actual == 'arriba'and stalker.posiciony <= self.posiciony:
                if self.recarga == 7:
                    pygame.mixer.music.play()
                    disparo = bala(self.posicionx, self.posiciony, actual)
                    disparos.add(disparo)
                    self.disparando = True
                    self.recarga = 0
        elif stalker.posiciony <= self.posiciony+29 <= stalker.posiciony+100:
            if actual == 'izquierda' and stalker.posicionx <= self.posicionx:
                if self.recarga == 7:
                    pygame.mixer.music.play()
                    disparo = bala(self.posicionx-1, self.posiciony, actual)
                    disparos.add(disparo)
                    self.disparando = True
                    self.recarga = 0
            if actual == 'derecha' and stalker.posicionx >= self.posicionx+50:
                if self.recarga == 7:
                    pygame.mixer.music.play()
                    disparo = bala(self.posicionx+5, self.posiciony, actual)
                    disparos.add(disparo)
                    self.disparando = True
                    self.recarga = 0
        else:
            self.disparando = False

        if self.alerta == False and self.disparando == False:
            if self.esperar == 0:
                self.eleccion = random.randint(0,4)
                self.esperar = random.randint(0,10)+10
            if self.eleccion == 1:
                if self.posiciony-5 <= 0:
                    self.eleccion = random.randint(2,4)
                else:
                    self.posiciony += -5
                    self.rect.y = self.posiciony
                    self.esperar += -1
                    estado = int(self.posicion_estado.get('arriba'))
                    imagen = self.imagenes.subsurface(pygame.Rect(self.posicion_de_imagenes[estado]))
                    self.image = pygame.transform.scale(imagen, (50, 100))
                    estado = 0
                    while estado <= int(self.posicion_estado.get('arriba')):
                        estado += 1
    
                    if estado == 8:
                        estado = 6

                    self.posicion_estado['arriba'] = estado
                    self.posicion_estado['actual'] = 'arriba'
            elif self.eleccion == 2:
                if self.posiciony+100 >= 600:
                    self.eleccion = random.randint(3,4)
                else:
                    self.posiciony += 5
                    self.rect.y = self.posiciony
                    self.esperar += -1
                    estado = int(self.posicion_estado.get('abajo'))
                    imagen = self.imagenes.subsurface(pygame.Rect(self.posicion_de_imagenes[estado]))
                    self.image = pygame.transform.scale(imagen, (50, 100))
                    estado = 0
                    while estado <= int(self.posicion_estado.get('abajo')):
                        estado += 1

                    if estado == 3:
                        estado = 0

                    self.posicion_estado['abajo'] = estado
                    self.posicion_estado['actual'] = 'abajo'
            elif self.eleccion == 3:
                if self.posicionx -5 <= 0:
                    self.eleccion = 4
                else:
                    self.posicionx += -5
                    self.rect.x = self.posicionx
                    self.esperar += -1
                    estado = int(self.posicion_estado.get('izquierda'))
                    imagen = self.imagenes.subsurface(pygame.Rect(self.posicion_de_imagenes[estado]))
                    self.image = pygame.transform.scale(imagen, (int(15/0.26), 100))
                    estado = 0
                    while estado <= int(self.posicion_estado.get('izquierda')):
                        estado += 1

                    if estado == 5:
                        estado = 3

                    self.posicion_estado['izquierda'] = estado
                    self.posicion_estado['actual'] = 'izquierda'
            elif self.eleccion == 4:
                if self.posicionx +50 >= 900:
                    self.eleccion = random.randint(1,3)
                else: 
                    self.posicionx += 5
                    self.rect.x = self.posicionx
                    self.esperar += -1
                    estado = int(self.posicion_estado.get('derecha'))
                    imagen = self.imagenes.subsurface(pygame.Rect(self.posicion_de_imagenes[estado]))
                    self.image = pygame.transform.scale(imagen, (int(15/0.26), 100))
                    estado = 0
                    while estado <= int(self.posicion_estado.get('derecha')):
                        estado += 1

                    if estado == 11:
                        estado = 9

                    self.posicion_estado['derecha'] = estado
                    self.posicion_estado['actual'] = 'derecha'
            else:
                self.esperar += -1


        if self.alerta == True and self.disparando == False:
            if stalker.posicionx - self.posicionx < 0:
                distanciax = self.posicionx - stalker.posicionx
            else:
                distanciax = stalker.posicionx - self.posicionx

            if stalker.posiciony - self.posiciony < 0:
                distanciay = self.posiciony - stalker.posiciony
            else:
                distanciay = stalker.posiciony - self.posiciony

            if distanciax >= distanciay:
                if (stalker.posicionx - self.posicionx) < 0: #izq
                    self.posicionx += -5
                    self.rect.x = self.posicionx
                    estado = int(self.posicion_estado.get('izquierda'))
                    imagen = self.imagenes.subsurface(pygame.Rect(self.posicion_de_imagenes[estado]))
                    self.image = pygame.transform.scale(imagen, (int(15/0.26), 100))
                    estado = 0
                    while estado <= int(self.posicion_estado.get('izquierda')):
                        estado += 1

                    if estado == 5:
                        estado = 3
    
                    self.posicion_estado['izquierda'] = estado
                    self.posicion_estado['actual'] = 'izquierda'
                else:
                    self.posicionx += 5
                    self.rect.x = self.posicionx
                    estado = int(self.posicion_estado.get('derecha'))
                    imagen = self.imagenes.subsurface(pygame.Rect(self.posicion_de_imagenes[estado]))
                    self.image = pygame.transform.scale(imagen, (int(15/0.26), 100))
                    estado = 0
                    while estado <= int(self.posicion_estado.get('derecha')):
                        estado += 1

                    if estado == 11:
                        estado = 9

                    self.posicion_estado['derecha'] = estado
                    self.posicion_estado['actual'] = 'derecha'
            else:
                if (stalker.posiciony - self.posiciony) < 0: #arr
                    self.posiciony += -5
                    self.rect.y = self.posiciony
                    estado = int(self.posicion_estado.get('arriba'))
                    imagen = self.imagenes.subsurface(pygame.Rect(self.posicion_de_imagenes[estado]))
                    self.image = pygame.transform.scale(imagen, (50, 100))
                    estado = 0
                    while estado <= int(self.posicion_estado.get('arriba')):
                        estado += 1

                    if estado == 8:
                        estado = 6

                    self.posicion_estado['arriba'] = estado
                    self.posicion_estado['actual'] = 'arriba'
                else:
                    self.posiciony += 5
                    self.rect.y = self.posiciony
                    estado = int(self.posicion_estado.get('abajo'))
                    imagen = self.imagenes.subsurface(pygame.Rect(self.posicion_de_imagenes[estado]))
                    self.image = pygame.transform.scale(imagen, (50, 100))
                    estado = 0
                    while estado <= int(self.posicion_estado.get('abajo')):
                        estado += 1

                    if estado == 3:
                        estado = 0

                    self.posicion_estado['abajo'] = estado
                    self.posicion_estado['actual'] = 'abajo'
        
        if self.recarga < 7:
            self.recarga += 1
  

class Jugador(Personaje):
    def __init__ (self, vida, posicionx, posiciony, tipo_personaje):
        Personaje.__init__(self, vida, posicionx, posiciony, tipo_personaje)
        self.meta = False

    def accion (self, tecla, disparos):
        if tecla[pygame.K_UP] or tecla[pygame.K_w]:
            estado = self.posicion_estado.get('arriba')
            imagen = self.imagenes.subsurface(pygame.Rect(self.posicion_de_imagenes[int(estado)]))
            if (self.posiciony) >= 0 and self.posiciony - 5 >= 0:
                self.posiciony += -8
                self.rect.y = self.posiciony
                self.image = pygame.transform.scale(imagen, (50, 100))
                estado = 0
                while estado <= int(self.posicion_estado.get('arriba')):
                    estado += 1
            
                if estado == 3:
                    estado = 0

                self.posicion_estado['arriba'] = estado
                self.posicion_estado['actual'] = 'arriba'
            else:
                imagen = self.imagenes.subsurface(pygame.Rect(28, 1, 13, 32))
                self.image = pygame.transform.scale(imagen, (50, 100))
                self.posicion_estado['actual'] = 'arriba'

        elif tecla[pygame.K_DOWN] or tecla[pygame.K_s]:
            estado = self.posicion_estado.get('abajo')
            imagen = self.imagenes.subsurface(pygame.Rect(self.posicion_de_imagenes[int(estado)]))
            if (self.posiciony)+105 <= 600:         
                self.posiciony += 8
                self.rect.y = self.posiciony
                self.image = pygame.transform.scale(imagen, (50, 100))
                estado = 3
                while estado <= int(self.posicion_estado.get('abajo')):
                    estado += 1

                if estado == 6:
                    estado = 3
                self.posicion_estado['abajo'] = estado
                self.posicion_estado['actual'] = 'abajo'
            else:
                imagen = self.imagenes.subsurface(pygame.Rect(99, 1, 13, 32))
                self.posicion_estado['actual'] = 'abajo'
                self.image = pygame.transform.scale(imagen, (50, 100))

        elif tecla[pygame.K_LEFT] or tecla[pygame.K_a]:
            estado = self.posicion_estado.get('izquierda')
            imagen = self.imagenes.subsurface(pygame.Rect(self.posicion_de_imagenes[int(estado)]))            
            if (self.posicionx) >= 0 and self.posicionx - 5 >= 0:           
                self.posicionx += -8
                self.rect.x = self.posicionx
                self.image = pygame.transform.scale(imagen, (int(16/0.26), 100))
                estado = 6
                while estado <= int(self.posicion_estado.get('izquierda')):
                    estado += 1

                if estado == 9:
                    estado = 6
                self.posicion_estado['izquierda'] = estado
                self.posicion_estado['actual'] = 'izquierda'

            else:
                imagen = self.imagenes.subsurface(pygame.Rect(170, 1, 15, 32))
                self.posicion_estado['actual'] = 'izquierda'
                self.image = pygame.transform.scale(imagen, (int(16/0.26), 100))

        elif tecla[pygame.K_RIGHT] or tecla[pygame.K_d]:
            estado = self.posicion_estado.get('derecha')
            imagen = self.imagenes.subsurface(pygame.Rect(self.posicion_de_imagenes[int(estado)]))
            if (self.posicionx)+int(16/0.26) <= 900:          
                self.posicionx += 8
                self.rect.x = self.posicionx
                self.image = pygame.transform.scale(imagen, (int(16/0.26), 100))
                estado = 9
                while estado <= int(self.posicion_estado.get('derecha')):
                    estado += 1

                if estado == 12:
                    estado = 9
                self.posicion_estado['derecha'] = estado
                self.posicion_estado['actual'] = 'derecha'

            else:
                imagen = self.imagenes.subsurface(pygame.Rect(242, 1, 16, 32))
                self.posicion_estado['actual'] = 'derecha'
                self.image = pygame.transform.scale(imagen, (int(16/0.26), 100))
        else:
            estado = self.posicion_estado.get('actual')
            if estado == 'arriba':
                imagen = self.imagenes.subsurface(pygame.Rect(28, 1, 13, 32))
                self.image = pygame.transform.scale(imagen, (50, 100))
            if estado == 'abajo':
                imagen = self.imagenes.subsurface(pygame.Rect(99, 1, 13, 32))
                self.image = pygame.transform.scale(imagen, (50, 100))
            if estado == 'izquierda':
                imagen = self.imagenes.subsurface(pygame.Rect(170, 1, 16, 32))
                self.image = pygame.transform.scale(imagen, (int(16/0.26), 100))
            if estado == 'derecha':
                imagen = self.imagenes.subsurface(pygame.Rect(242, 1, 16, 32))
                self.image = pygame.transform.scale(imagen, (int(16/0.26), 100))
        
        if tecla[pygame.K_SPACE]:
            if self.recarga >= 12:
                pygame.mixer.music.play()
                disparo = bala(self.posicionx, self.posiciony, self.posicion_estado.get('actual'))
                disparos.add(disparo)
                self.recarga = 0

        if tecla[pygame.K_r]:
            self.recarga +=2

        self.recarga += 1

class bala(pygame.sprite.Sprite):
    def __init__ (self, posicionx, posiciony, direccion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5,5])
        self.image.fill((25,25,25))
        if direccion == 'arriba':
            self.posicionx = posicionx + 24
            self.posiciony = posiciony - 5
        elif direccion == 'abajo':
            self.posicionx = posicionx +24
            self.posiciony = posiciony +100
        elif direccion == 'izquierda':
            self.posicionx = posicionx -6
            self.posiciony = posiciony +29
        else:
            self.posicionx = posicionx +63
            self.posiciony = posiciony +29

        self.direccion = direccion
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.posicionx,self.posiciony)

    def mover(self):
        if self.direccion == 'arriba':
            self.posiciony += -15
            self.rect.y = self.posiciony
    
        if self.direccion == 'abajo':
            self.posiciony += 15
            self.rect.y = self.posiciony

        if self.direccion == 'izquierda':
            self.posicionx += -15
            self.rect.x = self.posicionx

        if self.direccion == 'derecha':
            self.posicionx += 15
            self.rect.x = self.posicionx

def crearobjetos():
    objetos = pygame.sprite.Group()
    arbol = Objeto(1,0,0)
    objetos.add(arbol)
    arbol = Objeto(1,250,400)
    objetos.add(arbol)
    arbol = Objeto(1,850,480)
    objetos.add(arbol)
    arbol = Objeto(1,650,210)
    objetos.add(arbol)
    arbol = Objeto(1,210,230)
    objetos.add(arbol)
    arbol = Objeto(1,230,0)
    objetos.add(arbol)
    arbol = Objeto(1,600,0)
    objetos.add(arbol)
    caja = Objeto(2,110,130)
    objetos.add(caja)
    caja = Objeto(2,110,400)
    objetos.add(caja)
    caja = Objeto(2,650,450)
    objetos.add(caja)
    caja = Objeto(2,650,450)
    objetos.add(caja)
    caja = Objeto(2,350,320)
    objetos.add(caja)
    caja = Objeto(2,870,10)
    objetos.add(caja)

    return objetos

class Objeto(pygame.sprite.Sprite):
    def __init__ (self,o,x,y):
        pygame.sprite.Sprite.__init__(self)
        if o == 1:
            self.image = pygame.image.load(os.path.join('Images', 'Arbol.png'))
            self.image = pygame.transform.scale(self.image, (50,120))
            self.rect = self.image.get_rect()
            self.rect = self.rect.move(x,y)
        elif o == 2:
            self.image = pygame.image.load(os.path.join('Images', 'caja.png'))
            self.image = pygame.transform.scale(self.image, (40, 50))
            self.rect = self.image.get_rect()
            self.rect = self.rect.move(x,y)
        elif o==3:
            self.image = pygame.image.load(os.path.join('Images', 'targeta.png'))
            self.image = pygame.transform.scale(self.image, (30,20))
            self.rect = self.image.get_rect()
            self.rect = self.rect.move(x,y)

class Hud_f:
    def __init__(self):
        self.rgb = (50,0,0)
        self.imagen = pygame.image.load(os.path.join('Images', 'pasto.jpg'))
        self.imagen = pygame.transform.scale(self.imagen, (50,50))

def pintar (lista_personajes, pantalla, HUD, disparos, objetos,targeta):
    pantalla.fill((255, 255, 255))
    x = 0
    y = 0
    while y<= 12:
        while x <= 18:
            pantalla.blit(HUD.imagen,((x)*50,(y)*50))
            x += 1
        y += 1
        x = 0
    
    targeta.draw(pantalla)
    pygame.draw.rect(pantalla, HUD.rgb, pygame.Rect(0, 600, 900, 50))
    disparos.draw(pantalla)
    lista_personajes.draw(pantalla)
    objetos.draw(pantalla)
    pygame.display.update()



def iniciarjuego(pantalla, HUD, tecla, clock, objetos):
    i = False
    disparos = pygame.sprite.Group()
    pygame.mixer.music.load(os.path.join('Images', 'AK.wav'))
    stalker = Jugador(20, 0, 299, True)
    lista_personajes = pygame.sprite.Group()
    lista_personajes.add(stalker)
    Spetznas = pygame.sprite.Group()
    Spetzna = Enemigo(20,450,0, False)
    Spetznas.add(Spetzna)
    lista_personajes.add(Spetzna)
    Spetzna = Enemigo(20,850,250, False)
    Spetznas.add(Spetzna)
    lista_personajes.add(Spetzna)
    Spetzna = Enemigo(20,450,500, False)
    Spetznas.add(Spetzna)      
    lista_personajes.add(Spetzna)
    Spetzna = Enemigo(20,450,300, False)
    Spetznas.add(Spetzna)      
    lista_personajes.add(Spetzna)
    t = pygame.sprite.Group() 
    targeta = Objeto(3,860,230)
    t.add(targeta)

    while not i:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or tecla[pygame.K_ESCAPE]:
                i = True

        for Spetsnax in Spetznas:
            Spetsnax.accion(stalker, disparos, objetos)

        for disparo in disparos:
            if (disparo.posicionx -10 <= 0 or disparo.posicionx +10 >= 900 
            or disparo.posiciony -10 <= 0 or disparo.posiciony +10 >= 600):
                disparos.remove(disparo)
            else:
                disparo.mover()
                pygame.sprite.groupcollide(disparos, lista_personajes, True, True)
                pygame.sprite.groupcollide(disparos, objetos, True, False)

        tecla = pygame.key.get_pressed()
        stalker.accion(tecla,disparos)
        pintar(lista_personajes, pantalla, HUD, disparos, objetos, t)
        clock.tick(15)



def main():
    pygame.init()
    pantalla = pygame.display.set_mode((900, 650))
    pygame.display.set_caption("S.T.A.L.K.E.R")
    tecla = pygame.key.get_pressed()
    HUD = Hud_f()
    clock = pygame.time.Clock()
    objetos = crearobjetos()
    iniciarjuego(pantalla, HUD, tecla, clock, objetos)

main()
