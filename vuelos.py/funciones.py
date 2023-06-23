#primera funcion cual define la creacion de la matriz o matrix 

def crearmatrix(filas,columnas):
    PuestosdeAvion = [[],[],[],[],[],[]]
    CONTADOR=1     
    for columna in range(columnas):
        for fila in range(filas):
            PuestosdeAvion[columna].append([(CONTADOR)])
            CONTADOR+=1
    return PuestosdeAvion
puestosdeAvion=crearmatrix(7,6)

#------------------------------------------------------------------------------------
def DatosPasajero():
    Nombre=(input("Ingrese su Nombre :")).upper()
    rutPasajero=int(input("Ingrese su RUT (sin guion):"))
    telefono=(int(input("Ingrese su Telefono :")))
    bancopasajero=(input("Ingrese su  Banco:")).upper()
    basededatospasajero=[Nombre,rutPasajero,telefono,bancopasajero]
    return basededatospasajero
DatosUsuario=DatosPasajero()


    
#------------------------------------------------------------------------------------  
def preciosVuelos():
    precioNormal=78900
    precioVIP=240000
    BaseDatosPrecios=[precioNormal,precioVIP]
    return BaseDatosPrecios
precios=preciosVuelos()

print(precios)

#------------------------------------------------------------------------------------
def Menu():
    
    opc1=int(input("1.Ingresar a menu \n2.salir \n"))
    while opc1 != 0:
        opc1 = opc1+1
        opc=int(input("***BIENVENIDO A MENU VUELOSDUOC***\n----Porfavor escoja una opcion----\n1.Ver asientos Disponibles\n2.Comprar asientos \n3.Anular vuelo \n4.Modificar datos de usuario\n5.salir \n"))  
        if opc ==1:
            print("\n")
            print("---------------------------------")
            print("ingreso a ver asientos disponibles ")
            print("---------------------------------")
            print(puestosdeAvion)
        elif opc ==2:
            print("\n")
            print("---------------------------------")
            print("ingreso a a comprar asientos")
            print("---------------------------------") 
            NumeroAsiento=int(input("porfavor seleciones un asiento :"))
            print(f"ha escogido {NumeroAsiento} ")
        

        elif opc ==3:
            print("\n")
            print("---------------------------------")
            print("ingreso a anular vuelo")
            print("---------------------------------")
        elif opc ==4:
            print("\n")
            print("---------------------------------")
            print("ingreso Modificar datos de pasajero")
            print("---------------------------------")
        elif opc ==5:
            print("\n")
            print("---------------------------------")
            print("Gracias por usar vuelosduoc")
            print("---------------------------------")
            break
   
        return opc1
    
Menu1=Menu()

    #------------------------------------------------------------------------------------

