import json
import os.path

def chequear_usuario(x, nombre_usuario):
    with open('usuario.json') as file:
        usuarios = json.load(file)
    for dato in usuarios:
        if nombre_usuario == dato.get('nombre_usuario'):
            x=True
            break
        else:
            x=False

    return x

def agregar_susuario():                                                        
    nombre_usuario = input("\nIngrese nombre de usuario: ")
    x=True
    while x == True:
        x =chequear_usuario(x, nombre_usuario)
        if x == True:
            nombre_usuario = input("usuario en uso ingrese otro: ")

    contraseña = input("ingrese contraseña: ")
    nombre = input("ingrese su nombre: ")
    apellido = input("ingrese su apellido: ")
    edad = input("ingrese su edad: ")
    direccion = input("ingrese su direccion: ")
    casa_de_estudio = input("ingrese su casa de estudios: ")
    with open('usuario.json') as file:
        usuarios = json.load(file)
    usuarios.append({
        'nombre_usuario': nombre_usuario,
        'contraseña': contraseña,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'direccion': direccion,
        'casa_de_estudio': casa_de_estudio
    })

    with open('usuario.json', 'w') as file:
        json.dump(usuarios, file)
    print("\nusuario agregado")

def iniciar_secion():
    nombre_usuario = input("ingrese usuario: ")
    x = False
    while x == False:
        x = chequear_usuario(x, nombre_usuario)
        if x == False:
            nombre_usuario = input("usuario no existe ingrese nuevamente: ")
        else:
            break
    with open('usuario.json') as file:
        usuarios = json.load(file)
    for dato in usuarios:
        if nombre_usuario == dato.get('nombre_usuario'):
                contraseña = input("ingrese contraseña: ")
                x = True
                while x == True:
                    if contraseña == dato.get('contraseña'):
                        inicio(dato)
                        break
                    else:
                        contraseña = input("contraseña incorrecta ingresela nuevamente(si desea salir ingrese (1)): ")
                        if contraseña == str(1):
                            break

def inicio(usuario):
    print("\n\n\nBienvenido ",usuario.get('nombre'))
    while True:
        x = input("\nDejar mensaje(1)\nLeer mensaje(2)\nVer Datos(3)\nCambiar sus datos(4)\nsalir(5)\n¿Que desea hacer?: ")
        if x == '1':
            if os.path.isfile('mensajes.json'):
                nombre_usuario = input("¿para quien es el mensaje (nombre de usuario)? (cancelar(1)): ")
                if nombre_usuario == '1':
                    break
                else:
                    x = False
                    while x == False:
                        x = chequear_usuario(x, nombre_usuario)
                        if x == False:
                            nombre_usuario = input("usuario no existe ingrese otro: ")
                        
                    asunto = input("ingrese el asunto: ")
                    cuerpo = input("ingrese el mensaje: ")
                    with open('mensajes.json') as file:
                        mensajes = json.load(file)
                    
                    mensajes.append({
                        'remitente': usuario.get('nombre'),
                        'destinatario': x,
                        'estado': False,
                        'asunto': asunto,
                        'cuerpo': cuerpo
                    })
                    with open('mensajes.json', 'w') as file:
                        json.dump(mensajes, file)
                    print("mensaje enviado")
            else:
                nombre_usuario = input("¿para quien es el mensaje (nombre de usuario)? (cancelar(1)): ")
                if nombre_usuario == '1':
                    break
                else:
                    x = False
                    while x == False:
                        x = chequear_usuario(x, nombre_usuario)
                        if x == False:
                            nombre_usuario = input("usuario no existe ingrese otro: ")
                        
                    asunto = input("ingrese el asunto: ")
                    cuerpo = input("ingrese el mensaje: ")
                    mensajes = []
                    mensajes.append({
                        'remitente': usuario.get('nombre'),
                        'destinatario': x,
                        'estado': False,
                        'asunto': asunto,
                        'cuerpo': cuerpo
                    })
                    with open('mensajes.json', 'w') as file:
                        json.dump(mensajes, file)
                    print("mensaje enviado")
        
        elif x == '2':
            if os.path.isfile('mensajes.json'):
                with open('mensajes.json') as file:
                    mensajes = json.load(file)
            else:
                print("¡no existe mensajes!")
        elif x == '3':
            break

        elif x == '4':
            break

        elif x == '5':
            break

        else:
            x = input("se equivoco ingrese nuevamente: ")
            

#main
print("Bienvenido")
while True:
    if os.path.isfile('usuario.json'):
        x= input("\nIniciar sesión (1) \nNuevo usuario (2) \nSalir (3) \ningrese opcion: ")
        if x == '1':
            iniciar_secion()
        elif x == '2':
            agregar_susuario()
        elif x == '3':
            break
        else:
            print("\nTe equivocaste :p\n\n")
    else:
        print('no existe base de datos')
        usuarios = []
        nombre_usuario = 'Admin'
        nombre = input('ingrese el nombre del admin: ')
        apellido = input("ingrese apellido del admin: ")
        contraseña = input("ingrese contraseña: ")
        edad = input("ingrese su edad: ")
        direccion = input("ingrese su direccion: ")
        casa_de_estudio = input("ingrese su casa de estudios: ")
        usuarios.append({
            'nombre_usuario': nombre_usuario,
            'contraseña': contraseña,
            'nombre': nombre,
            'apellido': apellido,
            'edad': edad,
            'direccion': direccion,
            'casa_de_estudio': casa_de_estudio
        })
        with open('usuario.json', 'w') as file:
            json.dump(usuarios, file)
        print("\nadmin agregado")
