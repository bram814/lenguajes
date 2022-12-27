
'''
fecha         Descripcion
----------    ---------------------------------------------------
21/12/2022    Modelo


'''

class Gramatica():    
    __nombre                = []                                    # Nombre del archivo
    __no_terminal           = []                                    # No terminales
    __terminal              = []                                    # Terminales
    __no_terminal_inicial   = []                                    # No Terminal Inicial
    __produccion            = []                                    # Producciones



    def __init__(self, _nombre, _no_terminal, _terminal, _no_terminal_inicial, _produccion):
        self.__nombre               = _nombre
        self.__no_terminal          = _no_terminal
        self.__terminal             = _terminal
        self.__no_terminal_inicial  = _no_terminal_inicial
        self.__produccion           = _produccion

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, _nombre):
        self.__nombre = _nombre

    # Obtiene los terminales
    def get_no_terminal(self):
        return self.__no_terminal
    
    # Agrega un no terminal.
    def add_no_terminal(self, _no_terminal):
        self.__no_terminal.append(_no_terminal)

    # Elimina un no terminal por posicion.
    def pop_no_terminal(self, _posicion):
        self.__no_terminal.pop(_posicion)

    # Obtiene los terminales
    def get_terminal(self):
        return self.__terminal
    
    # Agrega un terminal.
    def add_terminal(self, _terminal):
        self.__terminal.append(_terminal)

    # Elimina un terminal por posicion.
    def pop_terminal(self, _posicion):
        self.__terminal.pop(_posicion)

    # Obtiene los terminales
    def get_no_terminal_inicial(self):
        return self.__no_terminal_inicial
    
    # Agrega un terminal.
    def add_no_terminal_inicial(self, _no_terminal_inicial):
        self.__no_terminal_inicial.append(_no_terminal_inicial)

    # Elimina un terminal por posicion.
    def pop_no_terminal_inicial(self, _posicion):
        self.__no_terminal_inicial.pop(_posicion)

    # Obtiene los terminales
    def get_produccion(self):
        return self.__produccion
    
    # Agrega un terminal.
    def add_produccion(self, _produccion):
        self.__produccion.append(_produccion)

    # Elimina un terminal por posicion.
    def pop_produccion(self, _posicion):
        self.__produccion.pop(_posicion)






