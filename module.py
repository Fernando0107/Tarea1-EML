


menu = {"Sumar" : "x + y", "Restar" : "x - y"}

def gen_menu(dic):

    print("   --- Menu ---")

    for key, value in dic.items():
        print(key)

gen_menu(menu)

#anonima : lambda n: 