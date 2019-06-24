import pygame
import os.path
import random

class Personaje(pygame.sprite.Sprite):
    """
        La clase personaje, es la clase padre para la clase jugador y enemigo,
        contiene todos los atributos en comun y necesario para el juego utiliza
        el modulo sprite de pygame.

        Atributos:
            posicionx: Es un int que representa el lugar en x de la pantalla 
                       que tiene el personaje.
            posiciony: Es un int que representa el lugar en y de la pantalla 
                       que tiene el personaje.
            recarga: Es un int y es el contador que dereminara la velocidad de
                     disparo del personaje.
            tipo_personaje: Es un boleano que tine como fin determinar si el
                            el personaje es un enemigo o jugador, en caso de
                            ser juagor elegira distintas imagenes.
            imagenes: Es un surface que carga la imagen que contiene las
                      las imagenes a usar.
            posicion_de_imagenes: Es una lista que contiene todas las
                                  posciciones de las subimagenes dentro de
                                  imagenes.
            posicion_estado: Es un diccionario que sirve para recordar y
                             poder elegir la subimagen siguiente a la 
                             animacion del personaje y tambien ver la
                             direccion donde esta viendo el personaje.
            image: Es un surface que se utilizara para mostrar en la pantalla
            rect: Es un Rect que contiene el ancho, largo y posicion en el mapa
                  del objeto.
    """
    def __init__ (self, posicionx, posiciony, tipo_personaje):
        """ Metodo constructor de Personaje, recibe 3 parametros necesarios 
            para construir el personaje si tipo_personaje es False
            cargara las imagenes del enemigo en caso contrario seran del 
            jugador. 
        """
        pygame.sprite.Sprite.__init__(self)
        self.posicionx = posicionx
        self.posiciony = posiciony
        self.recarga = 12
        if tipo_personaje == True:
            self.imagenes = (
                pygame.image.load(os.path.join('Images','Sprite.png')))
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
            self.imagenes = (
                pygame.image.load(os.path.join('Images', 'Spriteenemigo.png')))
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
    """
        Clase enemigo, contiene acciones automatizadas contiene parametros para
        controlar la dificultad del juego.

        Atributos:
            alerta: Es un boleano que indica si el enemigo a visto al jugador.
            disparando: Es un boleano que indica si el enemigo esta disparando
                        y evita que tome otras acciones mientras lo realiza.
            esperar: Es un entero que sirve para contar el tiempo entre una
                     accion y otra.
            eleccion: Es un entero aleatorio que sirve para elegir entre una
                      accion y otra.
            recarga: Es un entero que sirve como contador entre un disparo y
                     otro, evitando que sean muy seguidos.
    """
    def __init__ (self, posicionx, posiciony, tipo_personaje):
        """
            Metodo constructor del enemigo, recibe como parametros los de la
            anterior clase personaje, los demas atributos son ya definidos
        """
        Personaje.__init__(self, posicionx, posiciony, tipo_personaje)
        self.alerta = False
        self.disparando = False
        self.esperar = 15
        self.eleccion = random.randint(0,5)
        self.recarga = 7

    def accion(self, stalker, disparos, objetos):
        """
            Este metodo ejecuta las acciones del enemigo de forma automatica,
            recibe 3 parametros la clase jugador (stalker), un grupo de
            sprites que contienes a los diparos (disparos) y otro grupo de 
            spites que contiene los objetos (objetos), no retorna ningun
            dato, solo modifica los parametros de la clase.
        """
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
                    imagen = self.imagenes.subsurface(
                        pygame.Rect(self.posicion_de_imagenes[estado]))
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
                    imagen = self.imagenes.subsurface(
                        pygame.Rect(self.posicion_de_imagenes[estado]))
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
                    imagen = self.imagenes.subsurface(
                        pygame.Rect(self.posicion_de_imagenes[estado]))
                    self.image = pygame.transform.scale(
                        imagen, (int(15/0.26), 100))
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
                    imagen = self.imagenes.subsurface(
                        pygame.Rect(self.posicion_de_imagenes[estado]))
                    self.image = pygame.transform.scale(
                        imagen, (int(15/0.26), 100))
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
                    imagen = self.imagenes.subsurface(
                        pygame.Rect(self.posicion_de_imagenes[estado]))
                    self.image = pygame.transform.scale(
                        imagen, (int(15/0.26), 100))
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
                    imagen = self.imagenes.subsurface(
                        pygame.Rect(self.posicion_de_imagenes[estado]))
                    self.image = pygame.transform.scale(
                        imagen, (int(15/0.26), 100))
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
                    imagen = self.imagenes.subsurface(
                        pygame.Rect(self.posicion_de_imagenes[estado]))
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
                    imagen = self.imagenes.subsurface(
                        pygame.Rect(self.posicion_de_imagenes[estado]))
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
    """
        Clase que representa al jugador, esta clase contiene los atributos de
        la anterior clase Personaje, no tiene otros atributos extra.
    """
    def __init__ (self, posicionx, posiciony, tipo_personaje):
        """
            Metodo construtor del Jugador solo recibe los parametros de la
            anterior clase.
        """
        Personaje.__init__(self, posicionx, posiciony, tipo_personaje)

    def accion (self, tecla, disparos):
        """
            Este metodo contiene todas las acciones que puede tomar el jugador
            recibe como parametro la tecla presionada por el jugador (tecla) y
            un grupo de sprites que contiene los disparos (disparos), no
            retorna ningun dato, solo modifica los parametros de la clase.
        """
        if tecla[pygame.K_UP] or tecla[pygame.K_w]:
            estado = self.posicion_estado.get('arriba')
            imagen = self.imagenes.subsurface(
                pygame.Rect(self.posicion_de_imagenes[int(estado)]))
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
            imagen = self.imagenes.subsurface(
                pygame.Rect(self.posicion_de_imagenes[int(estado)]))
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
            imagen = self.imagenes.subsurface(
                pygame.Rect(self.posicion_de_imagenes[int(estado)]))            
            if (self.posicionx) >= 0 and self.posicionx - 5 >= 0:           
                self.posicionx += -8
                self.rect.x = self.posicionx
                self.image = pygame.transform.scale(
                    imagen, (int(16/0.26), 100))
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
            imagen = self.imagenes.subsurface(
                pygame.Rect(self.posicion_de_imagenes[int(estado)]))
            if (self.posicionx)+int(16/0.26) <= 900:          
                self.posicionx += 8
                self.rect.x = self.posicionx
                self.image = pygame.transform.scale(
                    imagen, (int(16/0.26), 100))
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
                self.image = pygame.transform.scale(
                    imagen, (int(16/0.26), 100))
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
                self.image = pygame.transform.scale(
                    imagen, (int(16/0.26), 100))
            if estado == 'derecha':
                imagen = self.imagenes.subsurface(pygame.Rect(242, 1, 16, 32))
                self.image = pygame.transform.scale(
                    imagen, (int(16/0.26), 100))
        
        if tecla[pygame.K_SPACE]:
            if self.recarga >= 12:
                pygame.mixer.music.play()
                disparo = bala(self.posicionx, self.posiciony, 
                    self.posicion_estado.get('actual'))
                disparos.add(disparo)
                self.recarga = 0

        if tecla[pygame.K_r]:
            self.recarga +=2

        self.recarga += 1

class bala(pygame.sprite.Sprite):
    """
        Clase que representa una bala dentro del juego, utiliza el modulo
        sprite.
        
        Atributos:
            image: Es un surface y la imagen de la bala.
            posicionx: Es un entero que sirve para ubicar en el eje x la
                       posicion de la bala.
            posiciony: Es un entero que sirve para ubicar en el eje y la
                       posicion de la bala.
            direccion: Es un string y sirve para indicar la trayectoria de la
                       bala durante el juego
            rect: Es un rect que contiene el ancho, largo y posicion de la
                  imagen y que utilizara en el juego.
    """
    def __init__ (self, posicionx, posiciony, direccion):
        """
            Metodo constructor de la clase bala y que recibe como parametro un
            entero para la posicion en x (posicionx), otro entero para la
            posicion en y (posiciony) y el string para reprecentar la 
            trayectoria (direccion), los parametros recibidos son de los 
            personajes.
        """
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
        """
            Este metodo sirve para mover cada bala en pantalla solo cambia los
            parametros de la clase, por lo que no recibe otro parametros, no
            retorna ningun dato.
        """
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
    """
        Crear objeto
        
        Esta funcion crea cara objeto dentro del juego, no recibe ningun
        parametro, cada objeto esta predefinido.
        
        Retorna:
            Un grupo de sprites que contiene cada objeto dentro del juego.
    """
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
    """
        Esta clase sirve para crear cada objeto en el juego, contiene 3
        opciones de creacion dependiendo que objeto se desee, utliza
        modulo sprite, como solo son objetos estaticos no tiene otros metodos.
        
        Atributos:
            image: Es un surface que sera la imagen del objeto.
            rect: Es un rect que contiene el ancho y largo de la imagen
                  como tambien su posicion tanto en x como en y.
    """
    def __init__ (self,o,x,y):
        """
            Metodo contructor de la clase recie 3 parametros, un entero que es
            para definir cual de los 3 objetos se usara (o), un entero para su
            posicion en x (x) y un ultimo entero para definir su posicion
            en y (y)
        """
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
            self.image = pygame.image.load(os.path.join(
                'Images', 'targeta.png'))
            self.image = pygame.transform.scale(self.image, (30,20))
            self.rect = self.image.get_rect()
            self.rect = self.rect.move(x,y)

class Hud_f:
    """
        Clase que contiene al hud y la imagen que se utlizara de fondo
        
        Atributos:
            rgb: Es una tupla que contiene el color en codigo RGB el color
                 que tendra de fondo el hud
            imagen: Es un surface que contiene la imagen de fondo del juego
                    en si.
    """
    def __init__(self):
        """
            Metodo constructor de la clase, no recibe ningun parametro, esta
            todo definido.
        """
        self.rgb = (50,0,0)
        self.imagen = pygame.image.load(os.path.join('Images', 'pasto.jpg'))
        self.imagen = pygame.transform.scale(self.imagen, (50,50))

def pintar (lista_personajes, pantalla, HUD, disparos, objetos,targeta):
    """
        Pintar

        Esta funcion se encarga de poner en pantalla cada una las imagenes que
        deberian estar en pantalla, no retorna ningun dato solo actualiza la
        pantalla

        Args:
            lista_personajes: Es un grupo de sprites que contiene cada
                              personaje en el juego.
            pantalla: Es la ventana en la cual se va a dibujar todas las
                      imagenes.
            HUD: es una clase que contiene el hud del juego y el fondo
            disparos: Es una lista de sprites que contien cada disparo para ser
                      dibujado.
            objetos: contiene cada objeto en pantalla que sera de obstaculo.s
            targeta: es una grupo de sprites que contiene un objeto especial.
        
        
        Retorna:
            no retorna ningun dato, solo actualiza la pantalla.
    """
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
    """
        Iniciar juego

        Esta funcion sirve para iniciar el juego y contiene el bucle
        infinito del juego que solo sera roto cerrando la pantalla o apretando
        la tecla ESC.

        Args:
            pantalla: Es la ventana por la cual se esta ejecutando el juego
            HUD: Es la clase que contiene el fondo y el hud del juego
            tecla: Es la funcion que detecta que tecla esta presionando el
                   jugador
            clock: Es un reloj para controlar la velociodad de la iteracion
                   del bucle o ciclo while
            objetos: Es un grupo de sprites que contiene cada objeto creado.
        
        Retorna:
            No retorna dato alguno, solo contiene el bucle del juego
    """
    i = False
    disparos = pygame.sprite.Group()
    pygame.mixer.music.load(os.path.join('Images', 'AK.wav'))
    stalker = Jugador(0, 299, True)
    lista_personajes = pygame.sprite.Group()
    lista_personajes.add(stalker)
    Spetznas = pygame.sprite.Group()
    Spetzna = Enemigo(450,0, False)
    Spetznas.add(Spetzna)
    lista_personajes.add(Spetzna)
    Spetzna = Enemigo(850,250, False)
    Spetznas.add(Spetzna)
    lista_personajes.add(Spetzna)
    Spetzna = Enemigo(450,500, False)
    Spetznas.add(Spetzna)      
    lista_personajes.add(Spetzna)
    Spetzna = Enemigo(450,300, False)
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
            Spetsnax.accion(stalker, disparos,objetos)

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
    """
        Main
        
        Es donde comienza todo, crea la vetana, el HUD, inicializa la espera de
        evento para el presionado de teclas, el reloj que se utilizara para
        controlar ciclos de iteracion y el grupo de objetos.
    """
    pygame.init()
    pantalla = pygame.display.set_mode((900, 650))
    pygame.display.set_caption("S.T.A.L.K.E.R")
    tecla = pygame.key.get_pressed()
    HUD = Hud_f()
    clock = pygame.time.Clock()
    objetos = crearobjetos()
    iniciarjuego(pantalla, HUD, tecla, clock, objetos)

main()
