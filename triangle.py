file = open("triangle.txt", "r")
x = []
temporal = 0

for line in file:

    x.append(line.split())


for i in range(len(x)):

    for j in range(len(x[i])):

        if (int(x[i][j + 1]) > int(x[i + 1][j + 1])):
            temporal += int(x[i][j + 1])
        else:
            temporal += int(x[i + 1][j + 1])


print(temporal)

"""
if (h == 0):
            h += int(x[i][j])

        if (len(x[i]) != 0 | i == len(x)):
            if (int(x[i][j]) > int(x[i + 1][j])):
                h += int(x[i][j])
            else:
                h += int(x[i+1][j])
# print(x[99][0])
"""
