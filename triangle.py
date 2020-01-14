file = open("triangle.txt", "r")
x = []
temporal = []

for line in file:

    x.append(line.split())


for i in range(len(x)):

    for j in range(len(x[i])):

        try:
            if (int(x[i][j]) > int(x[i + 1][j + 1])):
                temporal.append(int(x[i][j]))
            else:
                temporal.append(int(x[i + 1][j + 1]))

        except:
            pass

total = sum(temporal)
print(total)


"""
x[posicion de arrays][valor dentro del array]
"""
