#primera funcion cual define la creacion de la matriz o matrix 

def crearmatrix(filas,columnas):
    PuestosdeAvion = [[],[],[],[],[],[]]
    CONTADOR=1     
    for columna in range(columnas):
        for fila in range(filas):
            PuestosdeAvion[columna].append([(CONTADOR)])
            CONTADOR+=1
    return PuestosdeAvion
#puestosdeAvion=crearmatrix(7,6)

#------------------------------------------------------------------------------------
def DatosPasajero():
    Nombre=(input("Ingrese su Nombre :")).upper()
    rutPasajero=int(input("Ingrese su RUT (sin guion):"))
    telefono=(int(input("Ingrese su Telefono :")))
    bancopasajero=(input("Ingrese su  Banco:")).upper()
    basededatospasajero=[Nombre,rutPasajero,telefono,bancopasajero]
    return basededatospasajero
#DatosUsuario=DatosPasajero()


    
#------------------------------------------------------------------------------------  
def preciosVuelos():
    precioNormal=78900
    precioVIP=240000
    BaseDatosPrecios=[precioNormal,precioVIP]
    return BaseDatosPrecios
#precios=preciosVuelos()

#print(precios)

#------------------------------------------------------------------------------------
def MostrarVuelos(asientoVuelos):
    print("\n")
    print("---------------------------------")
    print("ingreso a ver asientos disponibles ")
    print("---------------------------------")
    print(asientoVuelos)
    #return"hola esto es un return y me devuelve un mensaje"
    #esto funciona como otra parte de codigo añadida 
    #print("esto no deberia salir")
#------------------------------------------------------------------------------------
def comprapasajes():
    print("---------------------------------")
    print("ingreso a a comprar asientos")
    print("---------------------------------")
    NumeroAsiento=int(input("porfavor seleciones un asiento :"))
    print("ha escojido el asiento :",NumeroAsiento)

#def Anularpasaje():
#def Modificardatos():

def anularVuelo():
    print("\n")
    print("---------------------------------")
    print("ingreso a anular vuelo")
    print("---------------------------------")
    print("ingrese sus datos")
