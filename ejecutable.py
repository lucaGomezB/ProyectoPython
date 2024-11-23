import Clases
#Acá se importa Clases.py

#*** A  C O N T I N U A C I O N  S E  C R E A N  L O S  M É T O D O S  D E  ejecutable.py  ***

def RellenarMatriz(matrizADN):
    #Este método rellena la matriz, en la matriz solo se admiten A, T, C o G
    baseNitrogenada = ""
    listaParaCompararBases = ["A","T","C","G"]
    for i in range(6):
        print("Porfavor ingrese 6 bases nitrogenadas (|A|, |T|, |C| o |G|), una por una.")
        cadenaDeBasesNitrogenadas = ""
        for j in range(6):
            while True:
                baseNitrogenada = input("Ingrese la próxima base nitrogenada : ")
                baseNitrogenada = baseNitrogenada.upper()
                if baseNitrogenada in listaParaCompararBases:
                    cadenaDeBasesNitrogenadas += baseNitrogenada
                    break
                else:
                    print("Porfavor ingrese solo A, T, C o G")
        matrizADN.append(cadenaDeBasesNitrogenadas)
    return matrizADN

def mostrarMatriz(matrizADN):
    #Este método muestra la matriz de forma elegante al usuario.
    for i in range(6):
        cadenaDeMatrizADN = matrizADN[i]
        for j in range(6):
            print(cadenaDeMatrizADN[j], end=" ")
        print()

def Menu(matrizADN):
    #Este método interactua con clases.py para modificar la matriz, detectar mutantes o mostrarla de vuelta
    detector = Clases.Detector(matrizADN)
    isMutante = detector.Detectar_mutantes(matrizADN)
    sanador = Clases.Sanador(matrizADN, isMutante)
    mutador = Clases.Mutador(matrizADN,isMutante)
    while True:
        print()
        print("------------------------------------------")
        print("               MENÚ PRINCIPAL          ")
        print("------------------------------------------")
        print("1. Detectar mutaciones")
        print("2. Mutar ADN")
        print("3. Sanar ADN")
        print("4. Mostrar ADN")
        print("5. Salir")
        print()
        opcion = input("Seleccione una opción : ")
        print()
        if opcion == "1":
           detector.Detectar_mutantes(matrizADN)
        elif opcion == "2":
            print("Qué desea realizar? ")
            opcion = input("1. Radiacion | 2. Virus : ")
            if opcion == "1":
                radiacion = Clases.Radiacion(mutador,detector.isMutante)
                baseNitrogenada = input("Porfavor ingrese la base nitrogenada que desea insertar : ")
                posicionInicialFila = input("Porfavor ingrese la fila de la posición inicial : ")
                posicionInicialColumna = input("Porfavor ingrese la columna de la posición inicial : ")
                orientacion = input("Porfavor ingrese la orientación : H. Horizontal | V. Vertical : ")
                matrizADN = radiacion.Crear_mutante(baseNitrogenada,posicionInicialFila,posicionInicialColumna,orientacion)
            elif opcion == "2":
                Clases.Virus(mutador,detector.isMutante)
        elif opcion == "3":
            matrizADN = sanador.Sanar_mutantes(matrizADN,detector.isMutante)
        elif opcion == "4":
            mostrarMatriz(matrizADN)
        elif opcion == "5":
            mostrarMatriz(matrizADN)
            print()
            print("Gracias por usar nuestro programa.")
            print()
            print("Crédito : ")
            print("Luca Gómez")
            break
        else:
            print("Porfavor elija una de las opciones.")


#**** A  C O N T I N U A C I O N  S E  E N C U E N T R A  E L  C Ó D I G O  P R I N C I P A L ****

matrizADN = []
print("Porfavor ingrese una matriz de ADN, tenga en cuenta que solo puede ingresar |A|, |T|, |C| o |G|")
matrizADN = RellenarMatriz(matrizADN)
print("Ha ingresado la matriz : ")
print()
mostrarMatriz(matrizADN)
print()
print("Porfavor ingrese un número para seleccionar la opción que desee : ")
print()
Menu(matrizADN)