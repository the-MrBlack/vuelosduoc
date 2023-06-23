import funciones as funcionVuelos

print("Bienvenido a vuelos duoc")
Ingresodatos=funcionVuelos.DatosPasajero()
#primero se crea matriz para indicializar los puestos de avion 
puestosdeAvion=funcionVuelos.crearmatrix(7,6)


opc1=int(input("1.Ingresar a menu \n2.salir \n"))
while opc1 != 0:
    opc1 = opc1+1
    opc=int(input("***BIENVENIDO A MENU VUELOSDUOC***\n----Porfavor escoja una opcion----\n1.Ver asientos Disponibles\n2.Comprar asientos \n3.Anular vuelo \n4.Modificar datos de usuario\n5.salir \n"))  
    if opc ==1:
        #primero se debe llamar la caja fuerte luego llamamos la funcion creada y le entregamos la variable que contiene la funcion en este caso puestosdeAvion
        respuesta=funcionVuelos.MostrarVuelos(puestosdeAvion)
        print(respuesta)
    elif opc ==2:
        print("---------------------------------")
        print("ingreso a a comprar asientos")
        print("---------------------------------")
        NumeroAsiento=int(input("porfavor seleciones un asiento :"))
        print("********************************************")
        print("ha escojido el asiento :",NumeroAsiento)
        print("********************************************")
    elif opc ==3:
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


