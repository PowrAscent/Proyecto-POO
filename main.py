from Funciones import Funciones

class Main:
    
    def __init__(self):
        self.f = Funciones()
        
    def ejecutarPrograma(self):
        self.f.menuMesaAyuda()
        
M = Main().ejecutarPrograma()