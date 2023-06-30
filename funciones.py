#funciones
def mostrar_menu():
    print("""MENÚ
    1. Grabar
    2. Buscar
    3. Retirarse
    4. Salir
    """)

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO!")

#crear variables necesarias:
import numpy
guarderia = numpy.zeros((2,5), int)
lista_ruts = []
lista_nombres = []
lista_nombre_mascota=[]
lista_filas = []
lista_columnas = []

#variables auxiliares:
lista_habitacion = ['A','B','C','D','E']
lista_pisos = [2,1]

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! RUT ENTRE 1000000 Y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
        lista_ruts.append(rut)

def validar_nombre():
    while True:
        nom = input("Ingrese nombre: ")
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")
        lista_nombres.append(nom)

def validar_mascota():
    while True:
        mascota = input("Ingrese nombre: ")
        if len(mascota.strip()) >= 3 and mascota.isalpha():
            return mascota
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")
        lista_nombre_mascota.append(mascota)

def validar_cant_dias():
    while True:
        try:
            dias=int(input("Ingrese la cantidad de dias que permanecerá en la guardería: "))
            if dias >=1:
                return dias
            else:
                print("ERROR! EL MINIMO DE DIAS ES 1")
        except:
            print("ERROR! DEBE INGRESAR UN NUMERO ENTERO!")

def ver_habitaciones():
    print("        A B C D E")
    for x in range(2):
        print("Piso",lista_pisos[x], end="\t")
        for y in range(5):
            print(guarderia[x][y], end=" ")
        print()

def validar_piso():
    while True:
        try:
            piso = int(input("Ingrese piso(1-2): "))
            if piso in lista_pisos:
                return piso
            else:
                print("ERROR! PISO INCORRECTO!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_habitacion():
    while True:
        habitacion = input("Ingrese habitacion:(1-10): ")
        if habitacion.upper() in lista_habitacion:
            return habitacion
        else:
            print("ERROR! DEPARTAMENTO INCORRECTO!")

def validar_id():
    orden=1
    for x in range (lista_ruts):
        lista_ruts[x]=orden
        orden=orden+1


def validar_compra():
    if 0 not in guarderia:
        print("NO EXISTEN DEPARTAMENTOS DISPONIBLES!")
        return
    rut = validar_rut()
    nombre = validar_nombre()
    while True:
        ver_habitaciones()
        piso = validar_piso()
        habitacion = validar_habitacion()
        piso_comprar = lista_pisos.index(piso)
        habitacion_comprar = lista_habitacion.index(habitacion.upper())
        if guarderia[piso_comprar][habitacion_comprar] == 0:
            total=validar_cant_dias*15000
            print("SU TOTAL A PAGAR ES: ")
            guarderia[piso_comprar][habitacion_comprar] = 1
            lista_ruts.append(rut)
            lista_nombres.append(nombre)
            lista_filas.append(piso_comprar)
            lista_columnas.append(habitacion_comprar)
            break
            
        else:
            print("DEPARTAMENTO NO DISPONIBLE")
