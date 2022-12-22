class Analizador():



    def __init__(self):
        pass

        
    


    def execute(self, _gramatica):
        
        
        count = 0

        nombre = []
        no_terminal = []
        terminal = []
        no_terminal_inicial = []
        producciones = []


        temp_nombre = ""
        temp_no_terminal = ""
        temp_terminales = ""

        for fila in _gramatica:
            # chr(txt) obtiene el chart
            for columna in fila:

                if ord(columna) == 10 : # <[10: \n ]> Salto de linea.

                    if count >= 4:
                        pass
                    
                    continue
                
                if ord(columna) == 37:  # <[37: % ]>. Finaliza gramatica.

                    count = -1                                  # Reiniciamos la gramatica.
                    
                    nombre.append(temp_nombre)                  # guardamos los nombres.
                    temp_nombre = ""                            # reiniciamos el temporal, para poder almacenar nuevamente el nombre de la gramatica.

                    no_terminal.append(temp_no_terminal)        # guardamos los no terminales.
                    temp_no_terminal = ""                       # reinciiamos el temporal, para poder almacenar nuevamente los no terminales de la gramatica.

                    terminal.append(temp_terminales)            # guardamos los terminales.
                    temp_terminales = ""                        # reinciiamos el temporal, para poder almacenar nuevamente los terminales de la gramatica.

                    continue                                    # sale del for columan, y vuelve a iniciar con la siguiente fila.

                
                if count == 0:          # Nombre de archivo
                    temp_nombre += chr(ord(columna))
                
                elif count == 1:        # No terminales     
                    
                    if ord(columna) != 44:          # <[44: , ]> 
                        temp_no_terminal += chr(ord(columna))

                elif count == 2:        # Terminales
                    if ord(columna) != 44:          # <[44: , ]> 
                        temp_terminales += chr(ord(columna))
                elif count == 3:        # No Terminal Inicial
                    pass

                elif count >= 4:        # Producciones
                    pass
            


            count += 1

        print(f"Nombre:             {nombre}")
        print(f"No Terminales:      {no_terminal}")
        print(f"Terminales:         {terminal}")



    def productions(self):
        pass