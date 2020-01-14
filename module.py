menu = {"1. Sumar": lambda x, y: x + y, "2. Restar": lambda x,
        y: x - y, "3. Multiplicar": lambda x, y: x * y}

print("--- Menu ---\n" + "\n".join("{}".format(k) for k, v in menu.items()))

x = int(input("Ingrese una opción del menú: "))

if x not in list(range(1, len(menu.items()) + 1)):
    print("Opción no valida.")
else:
    print(menu[list(menu.keys())[x - 1]](1, 2))
