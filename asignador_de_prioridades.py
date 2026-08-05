import random
ids = []
nombres = []
categorias = []
prioridades = []
responsables = []
estados = []
fechas = []
descripciones = []
observaciones = []
#---------------------------------------------#
#--|menu_principal_asignador_de_prioridades|--#
#---------------------------------------------#
while True:
    print("menu principal asignador de prioridades")
    print("1) registrar elemento")
    print("2) editar elemento")
    print("3) eliminar elemento")
    print("4) buscar elemento")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #------------------------#
    #--|registrar_elemento|--#
    #------------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_elemento = 1
        else:
            id_elemento = ids[-1] + 1
        nombre = input("nombre: ")
        categoria = input("categoría: ")
        prioridad = input("prioridad (alta, media o baja): ")
        responsable = input("responsable: ")
        estado = input("estado (pendiente, en proceso o completado): ")
        fecha = input("fecha de registro: ")
        descripcion = input("descripción: ")
        observacion = input("observación: ")
        ids.append(id_elemento)
        nombres.append(nombre)
        categorias.append(categoria)
        prioridades.append(prioridad)
        responsables.append(responsable)
        estados.append(estado)
        fechas.append(fecha)
        descripciones.append(descripcion)
        observaciones.append(observacion)
        print("elemento registrado correctamente.")
        print("id:", id_elemento)
    #---------------------#
    #--|editar_elemento|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            print("editar elemento")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {prioridades[i]}")
            id_buscar = int(input("ingrese la id del elemento: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("prioridad:", prioridades[posicion])
                nombres[posicion] = input("nuevo nombre: ")
                categorias[posicion] = input("nueva categoría: ")
                prioridades[posicion] = input("nueva prioridad: ")
                responsables[posicion] = input("nuevo responsable: ")
                estados[posicion] = input("nuevo estado: ")
                fechas[posicion] = input("nueva fecha: ")
                descripciones[posicion] = input("nueva descripción: ")
                observaciones[posicion] = input("nueva observación: ")
                print("elemento actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_elemento|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            print("eliminar elemento")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {prioridades[i]}")
            id_buscar = int(input("ingrese la id del elemento: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del elemento")
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("prioridad:", prioridades[posicion])
                respuesta = input("¿desea eliminar este elemento? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    categorias.pop(posicion)
                    prioridades.pop(posicion)
                    responsables.pop(posicion)
                    estados.pop(posicion)
                    fechas.pop(posicion)
                    descripciones.pop(posicion)
                    observaciones.pop(posicion)
                    print("elemento eliminado correctamente.")
                else:
                    print("el elemento no fue eliminado.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_elemento|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            print("buscar elemento")
            id_buscar = int(input("ingrese la id del elemento: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("categoría:", categorias[posicion])
                print("prioridad:", prioridades[posicion])
                print("responsable:", responsables[posicion])
                print("estado:", estados[posicion])
                print("fecha:", fechas[posicion])
                print("descripción:", descripciones[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            alta = 0
            media = 0
            baja = 0
            pendientes = 0
            proceso = 0
            completados = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {prioridades[i]} | {estados[i]}")
                if prioridades[i].lower() == "alta":
                    alta += 1
                elif prioridades[i].lower() == "media":
                    media += 1
                elif prioridades[i].lower() == "baja":
                    baja += 1
                if estados[i].lower() == "pendiente":
                    pendientes += 1
                elif estados[i].lower() == "en proceso":
                    proceso += 1
                elif estados[i].lower() == "completado":
                    completados += 1
            print("estadísticas asignador de prioridades")
            print("cantidad de registros:", len(ids))
            print("prioridad alta:", alta)
            print("prioridad media:", media)
            print("prioridad baja:", baja)
            print("pendientes:", pendientes)
            print("en proceso:", proceso)
            print("completados:", completados)
            posicion = -1
            for i in range(len(ids)):
                if prioridades[i].lower() == "alta":
                    posicion = i
                    break
            if posicion == -1:
                posicion = random.randint(0, len(ids) - 1)
            print("registro prioritario")
            print("id:", ids[posicion])
            print("nombre:", nombres[posicion])
            print("categoría:", categorias[posicion])
            print("prioridad:", prioridades[posicion])
            print("responsable:", responsables[posicion])
            print("estado:", estados[posicion])
            print("fecha:", fechas[posicion])
            print("descripción:", descripciones[posicion])
            print("observación:", observaciones[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el asignador de prioridades.")
        break
    else:
        print("opción no válida.")