from CVerificador import Verificador
from Cjugador import Jugador


matriz=[
    [1,2,3],    
    [4,5,6],
    ['X','X','X']
]

miJugador= Jugador()

simbolo='O'
for _ in range(0,8):    
    simbolo=miJugador.seleccionarJugador(simbolo)
    print(simbolo)




        













        



