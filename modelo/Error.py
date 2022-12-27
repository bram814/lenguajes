class Error():
    
    
    def __init__(self, contador, fila, columna, caracter):
        self.__fila = fila
        self.__columna = columna
        self.__caracter = caracter
        self.__contador = contador

    def get_fila(self):
        return self.__fila 

    def set_fila(self,fila):
        self.__fila = fila

    def get_columna(self):
        return self.__columna

    def set_columna(self,columna):
        self.__columna = columna

    def get_caracter(self):
        return self.__caracter

    def set_caracter(self,caracter):
        self.__caracter = caracter

    def get_contador(self):
        return self.__contador

    def set_contador(self,contador):
        self.__contador = contador

 
    def __str__(self):
        return f"{self.__contador},{self.__fila},{self.__columna},{self.__caracter}"