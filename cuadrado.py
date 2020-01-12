import math

A = (0,0)
B = (0,0)
C = (0,0)
D = (0,0)

def cuadrado(a,b,c,d):

    z = dist(a, b)
    x = dist(a, c)
    z1 = dist(a, d)

    if z == z1:
        x1 = dist(b,d)

        if(x1==x):
            return("Es un cuadrado")
        else:
            return("No es un cuadrado.")
    else: 
        return("No es un cuadrado")


def dist(a, b):

    d = math.sqrt(((a[0]-b[0])**(2))+((a[1]-b[1])**2))

    return d

print(cuadrado(A,B,C,D))