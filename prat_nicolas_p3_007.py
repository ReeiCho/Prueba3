#prueba3

import funciones as fn

fn.mostrar_menu()
opcion=fn.validar_opcion()
if opcion==1:
    rut=fn.validar_rut
    nombre=fn.validar_nombre
    id=fn.validar_id
    mascota=fn.validar_mascota
    cant_dias=fn.validar_cant_dias
    fn.ver_habitaciones
    if 0 in fn.guarderia:
        fn.validar_habitacion
    else:
        print("ERROR! NO HAY HABITACIONES DISPONIBLES!")

elif opcion==2:
    buscar=int(input("Ingrese rut: "))
    if buscar in fn.lista_ruts:
        print(fn.lista_ruts[buscar],fn.lista_habitacion[buscar])
    else:
        print("ERROR! NO HAY REGISTRO!")
    
elif opcion==3:
    fn.validar_compra

else:
    print("¡Gracias por su visita!")

