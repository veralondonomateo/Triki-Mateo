import random

class Jugador:
    
    def realizarJugada(self):
        #TO DO ¿De donde sale la matriz? 
        simbolo=self.seleccionarJugador()
        if simbolo == 'X':
            self.jugarComputador()
        else:
            self.jugarUsuario()           
                
    
    def seleccionarJugador(self,simbolo):
        if simbolo=='X':
            simbolo= 'O'
        else:
            simbolo ='X'
        return simbolo
            
    
    def jugarUsuario(self,tablero,simbolo):
        
        terminar=False
        
        while not terminar: #'terminar==False'
            #Pedir dos numeros al usuario
            x=int(input("ingresar X: "))
            y=int(input("ingresar Y: "))
            #
            if not tablero[x][y]== 'O' or tablero [x][y]=='X':
                terminar = True
            
                
        tablero[x][y]=simbolo
            
        return tablero
    
    def jugarComputador(self,tablero,simbolo):
        
        terminar=False
        
        while not terminar:
        
            x=random.randint(0,2)
            
            y=random.randint(0,2)
            
            if not tablero[x][y]== 'O' or tablero [x][y]=='X':
                terminar = True
        tablero[x][y]=simbolo
        return tablero
    
