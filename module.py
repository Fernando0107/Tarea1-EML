menu = {
    "1. Sumar": lambda x, y: x + y,
    "2. Restar": lambda x, y: x - y,
    "3. Multiplicar": lambda x, y: x * y
}


def gen_menu(dic):
    """
    gen_menu:
        Funcion que genera menus de manera dinamica.
    """
    print("--- Menu ---\n" + "\n".join("{}".format(k)
                                       for k, v in menu.items()))

    x = int(input("Ingrese una opción del menú: "))

    if x not in list(range(1, len(dic.items()) + 1)):
        return("Opción no valida.")
    else:
        return(menu[list(dic.keys())[x - 1]](1, 2))


print(gen_menu(menu))
