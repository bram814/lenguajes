from tkinter import filedialog
from io import open

from controlador.Analizador import Analizador

class Archivo():


    __analizador = Analizador()
  
    def __init__(self):
        self.__analizador = Analizador()

    def open_File(self):
            try:
           
                ruta =  ""
                filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("TXT files","*.glc"),("all files","*.*")))
                ruta = filename
                if ruta != "":
                    self.cargar_Archivo(ruta)
                    return ruta
                else:
                    
                    return None

            except IndexError as e:
                print(e)   

    def cargar_Archivo(self,ruta):
        print(f"Ruta: {ruta}")
        try:
        
            archivo = open(f"{ruta}","r", encoding="utf-8")
            texto = archivo.readlines()
            archivo.close()
            print(f"Texto:{texto}")

            
            self.__analizador.execute(texto)
            
        except (FileNotFoundError):
            print("Error")


    