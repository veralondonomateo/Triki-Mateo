import random
import os
import time

from numpy import matrix

def inicio_JUEGO():
    print("XOXO**********BIENVENIDO**********XOXO")
    time.sleep(1)
    while True:
        ficha= input("Seleccione ficha: X/O\n")
        ficha= ficha.upper()
        if ficha=="X":
            humano="X"
            computador="O"
            break
        elif ficha== "O":
            humano="O"
            computador="X"
            break
        else:
            print("por favor, inserte una ficha posible")
def tablero():
    print("triqui")
    print()
    print("     |     |     ")
    print("1  {}   |2  {}   |3  {}   ".format(matrix[0],matrix[1],matrix[2]))
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("4  {}   |5  {}   |6  {}   ".format(matrix[3],matrix[4],matrix[5]))
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("7  {}   |8  {}   |9  {}   ".format(matrix[6],matrix[7],matrix[8]))
    print("     |     |     ")
def empate(matriz):
    empate=True
    i=0
    while(empate==True and i<9):
        if matriz[i]==" ":
            empate=False
        i=i+1

    return empate

def victoria(matriz):
    if(matriz[0]==matriz[1]==matriz[2]!=" " 
    or matriz[3]==matriz[4]==matriz[5]!=" " 
    or matriz[6]==matriz[7]==matriz[8]!=" "
    or matriz[0]==matriz[3]==matriz[6]!=" "
    or matriz[1]==matriz[4]==matriz[7]!=" "
    or matriz[2]==matriz[5]==matriz[8]!=" "
    or matriz[0]==matriz[4]==matriz[8]!=" "
    or matriz[2]==matriz[4]==matriz[6]!=" "):
    return True
else:
    return False

def movimiento_jugador():
    while True:
        posiciones=[1,2,3,4,5,6,7,8,9]
        casilla=int(input("Seleccione casilla: "))
        if casilla not in posiciones:
            print("casilla no disponible ")

        else:
            if matriz[casilla-1]==" ":
                matriz[casilla-1]==humano
                break
            else:
                print("Casilla no disponible")


def movimiento_ordenador():
    posiciones=[1,2,3,4,5,6,7,8,9]
    casilla=9
    parar=False

    for i in posiciones:
        copia=list(matriz)
        if copia[i]==" ":
            copia[i]=ordenador
            if victoria(copia)==True:
                casilla=1

    if casilla==9:
        for j in posiciones:
            if copia[i]==" ":
            copia[i]=humano
            if victoria(copia)==

        













        



