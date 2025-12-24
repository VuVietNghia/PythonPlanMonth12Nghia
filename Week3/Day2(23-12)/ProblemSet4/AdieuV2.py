def adieu():
    this_list = []
    while True:
        name = input("Name(x): ")
        if name.lower() == 'x':
            break
        if name:
            this_list.append(name)

    formatted_list = ', '.join(this_list)
    print(f"Adieu, adieu, to {formatted_list}")

adieu()
