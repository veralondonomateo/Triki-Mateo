class Verificador:
    
    def __init__(self):
        self.triqui= False
        self.matriz=''
        
    def verificarTriqui(self):
        self.triqui=self.verificarFilas
        
        if not self.triqui:
            self.triqui=self.verificarColumnas
        if not self.triqui:
            self.triqui=self.verificarFilas
        if not self.triqui:
            self.triqui=self.verificarDiagonales  
            
    
    def verificarFilas(self, tablero):
        for fila in range (0,3):
            if tablero [fila][0]==tablero[fila][1] and tablero[fila][0]==tablero[fila][2]:
                self.triqui=True
            
            return self.triqui
        
                
    
    def verificarColumnas(self,tablero):
        for columna in range (0,3):
            if tablero [columna][0]==tablero[columna][1] and tablero[columna][0]==tablero[columna][2]:
                self.triqui=True
            
            return self.triqui
    
    def verificarDiagonales(self,tablero):
       
            if tablero [0][0]==tablero[1][1] and tablero[0][0]==tablero[2][2]:
                
                self.triqui=True
            if tablero [0][2]==tablero [1][1] and tablero [0][2]==tablero [2][0]:
                self.triqui=True


