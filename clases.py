class Detector():
    def __init__(self, matrizADN, isMutante):
        self.matrizADN = matrizADN
        self.isMutante = isMutante
        print("Detector ha sido instanciado")

    def detectar_Mutantes(self, matrizADN ,isMutante):
        if isMutante:
            print("Su matriz de ADN es mutante.")
        else:
            if detectarMutanteHorizontal(matrizADN):
                isMutante = True
                print("Su matriz de ADN contiene un mutante horizontal.")
                return isMutante
            elif detectarMutanteVertical(matrizADN):
                isMutante = True
                print("Su matriz de ADN contiene una mutante vertical.")
            elif detectarMutanteDiagonal(matrizADN):
                isMutante = True
                print("Su matriz de ADN contiene una mutante diagonal.")
            else:
                print("Su matriz de ADN no contiene mutantes.")
             

def detectarMutanteHorizontal(matrizADN):
    #Este método detecta si un caracter se repite en una fila.
    for fila in matrizADN:
        for i in range(len(fila) - 3):  
            if fila[i] == fila[i+1] == fila[i+2] == fila[i+3]:
                return True
    return False

def detectarMutanteVertical(matrizADN):
    #Este metodo detecta si un caracter se repite en una columna
    for j in range(6):
        for i in range(3):
            if matrizADN[i][j] == matrizADN[i+1][j] == matrizADN[i+2][j] == matrizADN[i+3][j]:
                return True
    return False

def detectarMutanteDiagonal(matrizADN):
    for i in range(3):
        for j in range(3):
            if matrizADN[i][j] == matrizADN[i+1][j+1] == matrizADN[i+2][j+2] == matrizADN[i+3][j+3]:
                return True
    for i in range(3):
        for j in range(3, 6):
            if matrizADN[i][j] == matrizADN[i+1][j-1] == matrizADN[i+2][j-2] == matrizADN[i+3][j-3]:
                return True
    return False