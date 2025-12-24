import inflect

p = inflect.engine()

def adieu():
    list_names = []
    while True:
        try:
            name = input("Name: ")
            list_names.append(name)
        except EOFError:
            break

    my_list = p.join(list_names)
    print("Adieu, adieu, to", my_list)

adieu()
