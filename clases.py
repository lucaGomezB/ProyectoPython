#CLASE DETECTOR
class Detector():
    #Esta clase detecta si hay mutaciones en la "matriz" de ADN que se le pasa, o sea, repeticiones de 4 caracteres seguidos.
    def __init__(self, matrizADN):
        self.matrizADN = matrizADN
        self.isMutante = False
        #Es falso hasta que se demuestra lo contrario
    def Detectar_mutantes(self, matrizADN):
        #La versión de un Switch en Python funciona como un menú de detecciones, si bien la ejecución el lineal, detecta lo necesario.
        if detectarMutanteHorizontal(matrizADN):
            self.isMutante = True
            print("Su matriz de ADN contiene un mutante horizontal.")
        elif detectarMutanteVertical(matrizADN):
            self.isMutante = True
            print("Su matriz de ADN contiene una mutante vertical.")
        elif detectarMutanteDiagonal(matrizADN):
            self.isMutante = True
            print("Su matriz de ADN contiene una mutante diagonal.")
        else:
            self.isMutante = False
            print("Su matriz de ADN no contiene mutantes.")

             

def detectarMutanteHorizontal(matrizADN):
    #Este método detecta si un caracter se repite en una fila.
    for j in range(6):
        cadena = matrizADN[j]
        for i in range(3):
            if cadena[i] == cadena[i+1] == cadena[i+2] == cadena[i+3]:
                return True
    return False

def detectarMutanteVertical(matrizADN):
    #Este método detecta si un caracter se repite en una columna.
    for i in range(3):
        #Cada cadena sería matrizADN[i]
        cadena1=matrizADN[i]
        cadena2=matrizADN[i+1]
        cadena3=matrizADN[i+2]
        cadena4=matrizADN[i+3]
        for j in range(6):
            if cadena1[j] == cadena2[j] == cadena3[j] == cadena4 [j]:
                return True
    return False

def detectarMutanteDiagonal(matrizADN):
    #Este método detecta si un caracter se repite en las diagonales.
    for i in range(3):
        for j in range(3):
            if matrizADN[i][j] == matrizADN[i+1][j+1] == matrizADN[i+2][j+2] == matrizADN[i+3][j+3]:
                return True
    for i in range(3):
        j = 3
        while j >= 0:
            #Acá usé este bucle para que recorra las diagonales con el "eje de abscisas" al revés o negativo.  
            if matrizADN[i][j] == matrizADN[i+1][j-1] == matrizADN[i+2][j-2] == matrizADN[i+3][j-3]:
                return True
            j -= 1
    return False

#SUPERCLASE MUTADOR
class Mutador:
    baseNitrogenada = ""
    def __init__(self, matrizADN, isMutante):
        self.matrizADN = matrizADN
        self.isMutante = isMutante
    def Crear_mutante():
        pass

#CLASE RADIACION (HEREDA DE NUTADOR)
class Radiacion(Mutador):
    def __init__(self, matrizADN, isMutante):
        super().__init__(self, matrizADN, isMutante)
    def Crear_mutante(self, baseNitrogenada, posicionInicialFIla, posicionInicialColumna, orientacionDeLaMutacion):
        if orientacionDeLaMutacion.upper() == "V":
            try:
                self.matrizADN[posicionInicialFIla] = self.matrizADN[posicionInicialFIla][:posicionInicialColumna] + baseNitrogenada + self.matrizADN[posicionInicialFIla][posicionInicialColumna:]
                self.matrizADN[posicionInicialFIla+1] = self.matrizADN[posicionInicialFIla+1][:posicionInicialColumna] + baseNitrogenada + self.matrizADN[posicionInicialFIla+1][posicionInicialColumna+4:]
                self.matrizADN[posicionInicialFIla+2] = self.matrizADN[posicionInicialFIla+2][:posicionInicialColumna] + baseNitrogenada + self.matrizADN[posicionInicialFIla+2][posicionInicialColumna+4:]
                self.matrizADN[posicionInicialFIla+3] = self.matrizADN[posicionInicialFIla+3][:posicionInicialColumna] + baseNitrogenada + self.matrizADN[posicionInicialFIla+3][posicionInicialColumna+4:]
            except IndexError:
                self.matrizADN[posicionInicialFIla] = self.matrizADN[posicionInicialFIla][:posicionInicialColumna] + baseNitrogenada + self.matrizADN[posicionInicialFIla][posicionInicialColumna:]
                self.matrizADN[posicionInicialFIla-1] = self.matrizADN[posicionInicialFIla-1][:posicionInicialColumna] + baseNitrogenada + self.matrizADN[posicionInicialFIla-1][posicionInicialColumna+4:]
                self.matrizADN[posicionInicialFIla-2] = self.matrizADN[posicionInicialFIla-2][:posicionInicialColumna] + baseNitrogenada + self.matrizADN[posicionInicialFIla-2][posicionInicialColumna+4:]
                self.matrizADN[posicionInicialFIla-3] = self.matrizADN[posicionInicialFIla-3][:posicionInicialColumna] + baseNitrogenada + self.matrizADN[posicionInicialFIla-3][posicionInicialColumna+4:]
            finally:
                print("Su matriz ha sido mutada mediante radiación")
                return self.matrizADN
        elif orientacionDeLaMutacion.upper() == "H":
            try:
                cadena = self.matrizADN[posicionInicialFIla]
                cadena = cadena[posicionInicialColumna]+baseNitrogenada+cadena[posicionInicialColumna+4]
                self.matrizADN[posicionInicialFIla] = cadena
            except IndexError:
                cadena = self.matrizADN[posicionInicialFIla]
                cadena = cadena[posicionInicialColumna]+baseNitrogenada+cadena[posicionInicialColumna-4]
                self.matrizADN[posicionInicialFIla] = cadena
                return self.matrizADN
        else:
            print("Porfavor ingrese una opcion válida")
            return self.matrizADN

#CLASE VIRUS(HEREDA DE NUTADOR)
class Virus(Mutador):
    def __init__(self, matrizADN, isMutante):
        super.__init__(self, matrizADN, isMutante)
    
    
#CLASE SANADOR
class Sanador:
    #El método Sanar_mutantes detecta si hay mutantes y los corrije alternando entre 2 modos, para así evitar conflictos.
    #La aleatoriedad es otorgada por el usuario, debido a que no logré aleatorizar la matriz sencillamente.
    def __init__(self, matrizADN, isMutante):
        self.matrizADN = matrizADN
        self.isMutante = isMutante
    def Sanar_mutantes(self, matrizADN, isMutante):
        import random
        detector = Detector(matrizADN)
        basesNitrogenadas = ["A", "T", "G", "C"]
        detector.Detectar_mutantes(matrizADN) 
        if isMutante:
            while detector.isMutante:
                # Mientras que la matriz siga siendo mutante, esto se repetirá, asegurando que la curación sea total.
                if detectarMutanteHorizontal(matrizADN):
                    contador = 2
                    for j in range(6):
                        cadena = matrizADN[j]
                        for i in range(3):
                            if cadena[i] == cadena[i+1] == cadena[i+2] == cadena[i+3]:
                                if contador % 2 == 0:
                                    cadena = cadena[0]+"ATGC"+cadena[5]
                                else:
                                    cadena = cadena[0]+"CGTA"+cadena[5]
                            contador += 1
                            matrizADN[j] = cadena
                if detectarMutanteVertical(matrizADN):
                    for i in range(3):
                        for j in range(6):
                            if matrizADN[i][j] == matrizADN[i+1][j] == matrizADN[i+2][j] == matrizADN[i+3][j]:
                                # Encontramos una mutación en la columna j
                                nueva_cadena = ""
                                for k in range(4):
                                    nueva_cadena += random.choice("ATGC")
                                    matrizADN[i] = matrizADN[i][:j] + nueva_cadena + matrizADN[i][j:]
                                    matrizADN[i+1] = matrizADN[i+1][:j] + nueva_cadena + matrizADN[i+1][j+4:]
                                    matrizADN[i+2] = matrizADN[i+2][:j] + nueva_cadena + matrizADN[i+2][j+4:]
                                    matrizADN[i+3] = matrizADN[i+3][:j] + nueva_cadena + matrizADN[i+3][j+4:]
                else:
                    break
            print("Su matriz ha sido sanada.")
            return matrizADN
        else:
            print("Su matriz no necesita ser sanada, porque no es mutante.")
            return matrizADN                    