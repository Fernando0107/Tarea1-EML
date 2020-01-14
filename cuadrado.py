# librerias
import math

# Tuplas (puntos x, y)
A = (-2, 9)
B = (4, 6)
C = (1, 0)
D = (-5, 3)

# Funciones
def cuadrado(
        a, b,
        c, d):
    """
    cuadrado: 
        Funcion que recibe cuatro parametros de tipo tupla.
        Esta funcion calcula distancias entre puntos con 
        ayuda de una funcion auxiliar llamada dist.
        Esta funcion retorna si dadas estas 4 tuplas, cumplen
        con ser un cuadrado.
    """
    z = dist(a, b)
    x = dist(a, c)
    z1 = dist(a, d)

    if z == z1:

        x1 = dist(b, d)

        if(x1 == x):
            return("Es un cuadrado")
        else:
            return("No es un cuadrado.")
    else:
        return("No es un cuadrado")


def dist(a, b):
    """
    dist:
        Funcion que calcula la distancia entre 2 puntos.
        Recibe 2 parametros: 2 tuplas.
    math.sqrt:
        Raiz cuadrada de cierto parametro.
    """

    d = math.sqrt(
        ((a[0]
        - b[0])**(2))
        + ((a[1]
        - b[1])**2)
    )

    return d


print(cuadrado(A, B,
                C, D))
