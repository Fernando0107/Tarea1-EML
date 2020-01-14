menu = {"1. Sumar": lambda x, y: x + y, "2. Restar" : lambda x, y: x - y}

def gen_menu(dic):
    """
    gen_menu:
        Funcion que genera menus de manera dinamica.
    """

    print("   --- Menu ---")

    for key, value in dic.items():
        print(key)

        #print(menu[list(dic.keys())[1]](1,2))
    x = int(input("Ingrese una opción del menú: "))
    
    if x not in list(range(1, len(dic.items()) + 1)): 
        print("Opción no valida.")
    else:
        print(menu[list(dic.keys())[x - 1]](1, 2))

gen_menu(menu)

#anonima : lambda n: 
