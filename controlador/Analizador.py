from modelo.Gramatica import Gramatica

class Analizador():



    def __init__(self):
        pass

        
    


    def execute(self, _gramatica):
        
        

        count = 0

        nombre  = []
        no_terminal = []
        terminal = []
        no_terminal_inicial = []
        producciones = []


        temp_nombre = ""
        temp_no_terminal = ""
        temp_terminales = ""
        temp_no_terminal_inicial = ""
        temp_producciones = ""

        diccionario = {}

        # ASCII - en python
        # ord -> Equivale a un numero                   char a ord -> numero
        # chr -> Equivale a un caracter (Char)          ord a char -> caracter

        print("")
        for fila in _gramatica:

            for columna in fila:

                # vAscii = ord(columna)                   # numero
                # vCaracter = chr(ord(columna))           # caracter
                

                if ord(columna) == 10:  # <[10: \n ]> Salto de linea.

                    if count >= 4:
                        
                        producciones.append(temp_producciones)
                        temp_producciones = ""

                    continue

                
                if ord(columna) == 37:  # <[37: %]> 
                    # limpiar
                    nombre.append(temp_nombre)
                    temp_nombre = ""

                    no_terminal.append(temp_no_terminal)
                    temp_no_terminal = ""

                    terminal.append(temp_terminales)
                    temp_terminales = ""

                    no_terminal_inicial.append(temp_no_terminal_inicial)
                    temp_no_terminal_inicial = ""

                    print(f'[Nombre]:                  {nombre}')
                    print(f'[No Terminal]:             {no_terminal}')
                    print(f'[Terminal]:                {terminal}')
                    print(f'[No Terminal Inicial]:     {no_terminal_inicial}')
                    print(f'[Producciones]:            {producciones}')
                    print("--------------------------------")
                    
                    diccionario[nombre[0]] = Gramatica(nombre, no_terminal, terminal, no_terminal_inicial, producciones)

                    
                    nombre = []
                    no_terminal = []
                    terminal = []
                    no_terminal_inicial = []
                    producciones = []

                    count = -1
                    continue


                if count == 0:          # Nombre de archivo
                    temp_nombre += chr(ord(columna))
                
                elif count == 1:        # No terminales     
                    temp_no_terminal += chr(ord(columna))
                    
                elif count == 2:        # Terminales
                    temp_terminales += chr(ord(columna))

                elif count == 3:        # No Terminal Inicial
                    temp_no_terminal_inicial += chr(ord(columna))

                elif count >= 4:        # Producciones
                    temp_producciones += chr(ord(columna))
            
            count += 1



        entrada_gramatica = 'Grm1'
        print("-------------------- GRAMATICA -----------------------")



        print(diccionario[entrada_gramatica].get_nombre())
        print(diccionario[entrada_gramatica].get_no_terminal())
        print(diccionario[entrada_gramatica].get_terminal())
        print(diccionario[entrada_gramatica].get_no_terminal_inicial())
        print(diccionario[entrada_gramatica].get_produccion())



    def productions(self):
        pass