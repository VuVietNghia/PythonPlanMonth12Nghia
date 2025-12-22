def grocery_list():
    this_list = []
    while True:
        item = input("Enter item: ")
        if item.lower() == "x":
            break
        if item:
            this_list.append(item)

    this_dict = {}
    for item in this_list:
        if item in this_dict:
            this_dict[item] += 1
        else:
            this_dict[item] = 1

    for item in sorted(this_dict):
        print(this_dict[item], item)

grocery_list()
