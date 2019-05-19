import json
import os.path

def chequear_usuario(x, nombre_usuario):
    ''' chequear_usuario(Buleano, String) -> Buleano
    Revisa si el nombre de usuario ya se encuentra en la base de datos,
    de encontrarce en ella devuelve un 'False', si no devuelve un
    'True'.
    x = Buleano que se retorna como 'True' o 'False'.
    '''
    with open('usuario.json') as archivo:
        usuarios = json.load(archivo)
    for usuario in usuarios:
        if nombre_usuario == usuario.get('nombre_usuario'):
            x=True
            break
        else:
            x=False

    return x




def chequear_clave(x, contraseña, nombre_usuario):
    ''' chequear_clave(Buleano, String, String) -> Buleano
    Revisa si la clave ingresada es igual a la correspondiente del
    usuario ingresado con anterioridad y devuelve un 'True', en caso
    de ser diferente devuelve un 'False'.
    x = Buleano que se retorna como 'True' o 'False'.
    '''
    with open('usuario.json') as archivo:
        usuarios = json.load(archivo)
    for usuario in usuarios:
        if nombre_usuario == usuario.get('nombre_usuario'):
            if contraseña == usuario.get('contraseña'):
                x=True
                break
            else:
                x=False
    return x




def agregar_usuario():
    ''' 
    Revisa si la base de datos de los usuarios existe. Si existe, pide
    un nuevo nombre para usuario y lo envía a verificar si es que ya
    se encuentra o no en uso, de encontrarce en uso le pide otro nombre
    de usuario hasta que sea ingresado uno diferente de los ya
    registrados, luego pide una contraseña y sus datos personales,
    finalmente lo guarda todo en la base de datos de los usuarios. Si
    no existe, realiza el mismo proceso ya mencionado y crea una base
    de datos para los usuarios para luego guardar los datos obtenidos.
    x = Condición que se mantiene si el usuario ingresado ya está 
    registrado.
    '''
    if os.path.isfile('usuario.json'):
        nombre_usuario = input("\nIngrese nombre de usuario: ")
        x=True
        while x == True:
            x =chequear_usuario(x, nombre_usuario)
            if x == True:
                nombre_usuario = input("Usuario en uso ingrese otro: ")

        contraseña = input("Ingrese contraseña: ")
        nombre = input("Ingrese su nombre: ").capitalize()
        while nombre.isalpha() is False:
            nombre = input("Ingrese un nombre real: ").capitalize()
        apellido = input("Ingrese su apellido: ").capitalize()
        while apellido.isalpha() is False:
            apellido = input("Ingrese un apellido real: ").capitalize()
        edad = input("Ingrese su edad: ")
        while edad.isdigit() is False or 1 > int(edad) or  int(edad) > 110:
            edad = input("Ingrese una edad real en numeros: ")
        direccion = input("Ingrese su direccion: ").capitalize()
        casa_de_estudio = input("Ingrese su casa de estudios: ").capitalize()
        with open('usuario.json') as archivo:
            usuarios = json.load(archivo)
        usuarios.append({
	                   'nombre_usuario': nombre_usuario,
                        'contraseña': contraseña,
                        'nombre': nombre,
                        'apellido': apellido,
                        'edad': edad,
                        'direccion': direccion,
                        'casa_de_estudio': casa_de_estudio})

        with open('usuario.json', 'w') as archivo:
            json.dump(usuarios, archivo)
        print("\nUsuario agregado")
    else:
        print('\nNo existe base de datos')
        usuarios = []
        nombre_usuario = 'Admin'
        nombre = input('Ingrese el nombre del admin: ').capitalize()
        while nombre.isalpha() is False:
            nombre = input("Ingrese un nombre real: ").capitalize()
        apellido = input("Ingrese apellido del admin: ").capitalize()
        while apellido.isalpha() is False:
            apellido = input("Ingrese un apellido real: ").capitalize()
        contraseña = input("Ingrese contraseña: ")
        edad = input("Ingrese su edad: ")
        while edad.isdigit() is False or 1 > int(edad) or int(edad) > 110:
            edad = input("Ingrese una edad real en numeros: ")
        direccion = input("Ingrese su direccion: ").capitalize()
        casa_de_estudio = input("Ingrese su casa de estudios: ").capitalize()
        usuarios.append({
                        'nombre_usuario': nombre_usuario,
                        'contraseña': contraseña,
                        'nombre': nombre,
                        'apellido': apellido,
                        'edad': edad,
                        'direccion': direccion,
                        'casa_de_estudio': casa_de_estudio})
        with open('usuario.json', 'w') as archivo:
            json.dump(usuarios, archivo)
        print("\nAdmin agregado")    




def iniciar_sesion():
    '''
    Pide un nombre de usuario y envía a chequear este para ver si se
    encuentra en la base de datos, luego de comprobar que el usuario si
    se encuentre le pide la clave y la envía a verificar verificar, si
    todo se encuentra correcto le permitirá el acceso al menu (de
    usuario o de administrador dependiendo si el ingresado es 'Admin'
    o no), de lo contrario se lo negará.
    x = Condición que debe cumplirse.
    '''
    nombre_usuario = input("Ingrese usuario: ")
    x = False
    while x == False:
        x = chequear_usuario(x, nombre_usuario)
        if x == False:
            nombre_usuario = input("\nUsuario no existe ingrese nuevamente: ")
        else:
            x = True
    with open('usuario.json') as archivo:
        usuarios = json.load(archivo)
    for usuario in usuarios:
        if nombre_usuario == usuario.get('nombre_usuario'):
            break
    contraseña = input("Ingrese contraseña: ")
    x = False
    if nombre_usuario == "Admin":
        while x == False:
            x = chequear_clave(x, contraseña, nombre_usuario)
            if x == False:
                contraseña = input("contraseña equivocada ingrese nuevamente: ")
        menu_admin(usuario)
    else:
        while x == False:
            x = chequear_clave(x, contraseña, nombre_usuario)
            if x == False:
                contraseña = input("contraseña equivocada ingrese nuevamente: ")
        menu(usuario)




def dejar_mensaje(usuario):
    ''' dejar_mensaje(String)
    Cheaquea si existe la base de datos de los mensajes. Si existe,
    pregunta para cual usuario es el mensaje, cual es el asunto, cual
    es el mensaje y guadra todo en la base de datos de los mensajes.Si
    no existe, pregunta los datos anteriormente mencionados, crea la
    base de datos de los mensajes y guarda la información de este en
    ella.
    '''
    if os.path.isfile('mensajes.json'):
        nombre_usuario = input("¿Para quien es el mensaje" +
            " (nombre de usuario)?: ")
        x = False
        while x == False:
            x = chequear_usuario(x, nombre_usuario)
            if x == False:
                nombre_usuario = input("Usuario no existe ingrese otro: ")
						
        asunto = input("Ingrese el asunto: ")
        cuerpo = input("Ingrese el mensaje: ")
        with open('mensajes.json') as archivo:
            mensajes = json.load(archivo)
        mensajes.append({
                        'remitente': usuario.get('nombre_usuario'),
                        'destinatario': nombre_usuario,
                        'estado': False,
                        'asunto': asunto,
                        'cuerpo': cuerpo})
        with open('mensajes.json', 'w') as archivo:
            json.dump(mensajes, archivo)
        print("Mensaje enviado")
    else:
        nombre_usuario = input("¿Para quien es el mensaje" +
            " (nombre de usuario)?: ")
        x = False
        while x == False:
            x = chequear_usuario(x, nombre_usuario)
            if x == False:
                nombre_usuario = input("\nUsuario no existe, " +
                    "ingrese otro: ")

        asunto = input("Ingrese el asunto: ")
        cuerpo = input("Ingrese el mensaje: ")
        mensajes = []
        mensajes.append({
                        'remitente': usuario.get('nombre_usuario'),
                        'destinatario': nombre_usuario,
                        'estado': False,
                        'asunto': asunto,
                        'cuerpo': cuerpo})
        with open('mensajes.json', 'w') as archivo:
            json.dump(mensajes, archivo)
        print("Mensaje enviado")




def bandeja_de_entrada(usuario):
    ''' bandeja_de_entrada(String)
    Es la bandeja de entrada del usuario, en donde puede ver sus
    mensajes recibidos, quién es el remitente y el asunto de este, o
    si no tiene mensajes.
    El 'for' es para mostrar los mensajes no leidos con sus datos del
    archivo de mensajes.
    i = contador de mensajes.
    '''
    if os.path.isfile('mensajes.json'):
        with open('mensajes.json') as archivo:
            mensajes = json.load(archivo)
        mensaje_sin_leer = 0
        for mensaje in mensajes:
            if (mensaje.get('estado') == False and 
                mensaje.get('destinatario')==usuario.get('nombre_usuario')):
                mensaje_sin_leer = mensaje_sin_leer + 1
        print("Tiene ",mensaje_sin_leer," sin leer")
        i=0
        for mensaje in mensajes:
            if (mensaje.get('estado') == False and
                mensaje.get('destinatario') == usuario.get('nombre_usuario')):
                i = i+1
                print("\nMensaje:",i)
                print("De:", mensaje.get('remitente'))
                print("Asunto:", mensaje.get('asunto'))
                print(mensaje.get('cuerpo'))
                mensaje['estado']=True

        with open('mensajes.json', 'w') as archivo:
            json.dump(mensajes, archivo)
    else:
        print("No hay mensajes")




def menu(usuario):
    ''' menu(String)
    Menu del usuario, en el cual puede: Dejar un mensaje a algun otro
    usuario, ver si tiene mensajes recividos, ver sus datos.
    El 'while' hace de menu para las opciones hasta que se decida salir
    eligiendo la opcion para ello.
    '''
    print("\n\n\nBienvenido ",usuario.get('nombre'))
    while True:
        print("\nDejar mensaje (1)\nBandeja de entrada (2)\nVer sus datos(3)")
        x = input("Cerrar sesión (4)\n¿Que desea hacer?: ")
        if x == '1':
            dejar_mensaje(usuario)

        elif x == '2': #Bandeja de entrada
            bandeja_de_entrada(usuario)

        elif x == '3': #Ver datos sus datos
            print("\nNombre:",usuario.get('nombre'))
            print("Apellido:",usuario.get('apellido'))
            print("Edad:",usuario.get('edad'))
            print("Direccion:",usuario.get('direccion'))
            print("Casa de estudio:",usuario.get('casa_de_estudio'))

        elif x == '4':
            break
        else:
            print("¡Se equivoco, ingrese nuevamente!")




def menu_admin(usuario):
    ''' menu_admin(String)
    Menu del administrador, en el cual puede: Dejar un mensaje a algun
    otro usuario, ver si tiene mensajes recividos, ver sus datos,
    eliminar sus mensajes, eliminar los mensajes de otro usuario,
    eliminar a otro usuario.
    El 'while' hace de menu para las opciones hasta que se decida salir
    eligiendo la opcion para ello.
    '''
    print("\n\n\nBienvenido ",usuario.get('nombre'))
    while True:
        print("\nDejar mensaje(1)\nBandeja de entrada (2)\nVer sus datos(3)")
        print("Eliminar mensajes leidos(4)")
        print("Eliminar mensajes de un usuario(5)")
        x = input("Eliminar usuario(6)\nCerrar sesión(7)\n¿Que desea hacer?: ")
        if x == '1':
            dejar_mensaje(usuario)

        elif x == '2': #Bandeja de entrada
            bandeja_de_entrada(usuario)

        elif x == '3': #Ver datos sus datos
            print("\nNombre:",usuario.get('nombre'))
            print("Apellido:",usuario.get('apellido'))
            print("Edad:",usuario.get('edad'))
            print("Direccion:",usuario.get('direccion'))
            print("Casa de estudio:",usuario.get('casa_de_estudio'))

        elif x == '4':
            eliminar_mensajes_leidos()

        elif x == '5':
            print("Eliminara todos los mensajes asociados a ese usuario"
            +"ya sean enviados o recividos ¡¿Esta seguro?! ")
            x = input("(1) Si, cualquier tecla para cancelar): ")
            if x == '1':
                nombre_usuario = input("Ingrese usuario: ")
                x = False
                while x == False:
                    x = chequear_usuario(x, nombre_usuario)
                    if x == False:
                        nombre_usuario = input("Usuario no existe," +
                            " ingrese otro: ")
                eliminar_mensajes_de_usuario(nombre_usuario)
        elif x == '6':
            print("El usuario se eliminara y los mensajes igual"
            +"ya sean enviados o recividos ¡¿Esta seguro?! ")
            x = input("(1) Si, cualquier tecla para cancelar): ")
            if x == '1':
                nombre_usuario = input("Ingrese usuario: ")
                x = False
                while x == False:
                    x = chequear_usuario(x, nombre_usuario)
                    if x == False:
                        nombre_usuario = input("Usuario no existe,"+
                                            "ingrese otro: ")
                if nombre_usuario == "Admin":
                    print("No puede borrar Admin")
                else:
                    eliminar_mensajes_de_usuario(nombre_usuario)
                    eliminar_usuario(nombre_usuario)
                    print("Usuario eliminado")
        elif x == '7':
            break
        else:
            print("¡Se equivoco ingrese nuevamente!")




def eliminar_mensajes_leidos():
    ''' 
    Revisa que exista la base de datos de los mensajes, si existe
    elimina los mensajes, si no existe muestra que no hay mensajes
    por eliminar.
    Los 'for' son para borrar y asegurar de que todos los mensajes
    leidos sean borrados.
    '''
    if os.path.isfile('mensajes.json'):
        with open('mensajes.json') as archivo:
            mensajes = json.load(archivo)
        for mensaje in mensajes:
            if mensaje.get('estado') == True:
                mensajes.remove(mensaje)
        for mensaje in mensajes:
            if mensaje.get('estado') == True:
                mensajes.remove(mensaje)
        with open('mensajes.json','w') as archivo:
            json.dump(mensajes,archivo)
        print("Mensajes eliminados")
    else:
        print("No existe mensajes por eliminar")




def eliminar_mensajes_de_usuario(nombre_usuario):
    ''' eliminar_mensajes_de_usuario(String)
    Revisa si existe la base de datos de los mensajes, si existe
    elimina los mensajes dirigidos o emitidos por el usuario
    seleccionado, si no existe chequea si el usuario existe en la base
    de datos, de existir se muestra que el dicho usuario no tiene
    mensajes.
    El primer 'while' es para asegurar de que se hayan borrado los
    mensajes emitidos o dirigidos al usuario seleccionado. El segudno
    'while' es para asegurar de que el usuario ingresado esté
    reegistrado, y si está mostrar que no tiene mensajes.
    '''
    if os.path.isfile('mensajes.json'):
        with open('mensajes.json') as archivo:
            mensajes = json.load(archivo)
        x = False
        while x == False:
            for mensaje in mensajes:
                if (mensaje.get('remitente') == nombre_usuario or 
                    mensaje.get('destinatario') == nombre_usuario):
                    mensajes.remove(mensaje)
            if x == False:
                x = chequear_removicion_completa(x, mensajes, nombre_usuario)
        with open('mensajes.json','w') as archivo:
            json.dump(mensajes,archivo)
        print("\nMensajes eliminados")
        return nombre_usuario
    else:
        nombre_usuario = input("Ingrese usuario: ")
        x = False
        while x == False:
            x = chequear_usuario(x, nombre_usuario)
            if x == False:
                nombre_usuario = input("\nUsuario no existe, ingrese otro: ")
        print("\nNo existe mensajes por eliminar")
        return nombre_usuario




def chequear_removicion_completa(x, mensajes, nombre_usuario):
    ''' (Buleano, Lista, String) -> Buleano
    Revisa si hay algun mensaje escrito o dirigido hacia el usuario
    seleccionado, retorna 'False' si encuentra alguno o 'True' si no
    encuentra ninguno.
    El 'for' es para recorrer mensaje por mensaje cada uno de ellos del
    archivo de los mensajes. 
    '''
    for mensaje in mensajes:
        if (mensaje.get('remitente') == nombre_usuario or 
            mensaje.get('destinatario') == nombre_usuario):
            return x
    x = True
    return x




def eliminar_usuario (nombre_usuario):
    '''eliminar_usuario(String)
    Elimina de la base de datos al usuario seleccionado.
    El 'for' es para recorrer a los usuarios del archivo de usuarios.
    '''
    with open('usuario.json') as archivo:
        usuarios = json.load(archivo)
    for usuario in usuarios:
        if usuario.get('nombre_usuario') == nombre_usuario:
            usuarios.remove(usuario)
    with open('usuario.json', 'w') as archivo:
        json.dump(usuarios,archivo)



#main
print("Bienvenido")
while True:
    if os.path.isfile('usuario.json'):
        with open('usuario.json') as archivo:
            usuarios = json.load(archivo)
        for dic in usuarios:
            if dic.get('nombre_usuario') == 'Admin':
                clave = dic.get('contraseña')

        x= input("\nIniciar sesión (1) \nNuevo usuario (2)" +
            "\nSalir del programa (3) \nIngrese opcion: ")
        if x == '1':
            iniciar_sesion()
        elif x == '2':
            agregar_usuario()
        elif x == '3':
            break
        else:
            print("¡Se equivoco, ingrese nuevamente!\n")
    else:
        agregar_usuario()
