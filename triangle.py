file = open("triangle.txt", "r")
x = []

for line in file:

    x.append(line.split())


def triangulo(file):

    temporal = []

    for i in range(len(x)):

        for j in range(len(x[i]) - 1):

            mx = max(int(x[i][j]), int(x[i][j + 1]))

            temporal.append(mx)

    return sum(temporal)


print(triangulo(x))
"""
x[posicion de arrays][valor dentro del array]
"""
