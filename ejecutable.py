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
    for i in range(6):
        cadenaDeMatrizADN = matrizADN[i]
        for j in range(6):
            print(cadenaDeMatrizADN[j], end=" ")
        print()

def Menu(matrizADN):
    isMutante = False
    detector = Clases.Detector(matrizADN, isMutante)
    #Este método interactua con clases.py para modificar la matriz o mostrarla de vuelta
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
        opcion = int(input("Seleccione una opción : "))
        print()
        if opcion == 1:
           isMutante = detector.detectar_Mutantes(matrizADN,isMutante)
        elif opcion == 2:
            matrizADN
        elif opcion == 3:
            matrizADN
        elif opcion == 4:
            mostrarMatriz(matrizADN)
        elif opcion == 5:
            print("Gracias por usar nuestro programa.")
            print()
            print("Créditos : ")
            print(" L Rafael Ruiz")
            print(" L Luca Gómez")
            break


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